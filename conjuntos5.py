"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 4: SEGURIDAD - CONTROL DE ACCESO
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una empresa necesita un sistema de control de acceso basado en roles.
Cada rol tiene un conjunto de permisos. El sistema debe:

1. Verificar si un usuario puede realizar una acción
2. Encontrar permisos comunes entre roles
3. Encontrar permisos exclusivos de cada rol
4. Verificar si un rol es "superior" a otro (tiene todos sus permisos)
5. Crear un nuevo rol combinando permisos de otros

Implementar usando operaciones de conjuntos.

El Operador <= es tu mejor amigo: En seguridad,
casi siempre la pregunta es "¿Tiene permiso?". Eso se traduce automáticamente en:
acciones_necesarias <= mis_permisos.

Conflictos de Seguridad: Siempre que te pidan "validar si algo es peligroso",
piensa en una Intersección (&) contra una lista negra (blacklist).
Si la intersección da algo, hay peligro.

Cuidado con get(): En el código se usa usuarios.get(usuario).
Esto es para que el programa no falle si el usuario no existe (devuelve None en lugar de un error).
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════
# Cada rol es un conjunto de strings (permisos).
roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"},
}

usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SEGURIDAD - CONTROL DE ACCESO")
print("=" * 60)

print("\nRoles y permisos:")
for rol, permisos in roles.items():
    print(f"  {rol}: {sorted(permisos)}")

print("\nUsuarios:")
for usuario, rol in usuarios.items():
    print(f"  {usuario} → {rol}")


# 1. VERIFICAR ACCESO (Subconjuntos <=)
# Para saber si alguien puede entrar, preguntamos:
# "¿Están las 'acciones_requeridas' DENTRO de sus 'permisos'?"
print("\n" + "=" * 60)
print("1. VERIFICAR ACCESO")
print("=" * 60)

def puede_hacer(usuario, acciones_requeridas):
    """Verifica si el usuario tiene todos los permisos necesarios"""
    rol = usuarios.get(usuario)
    if not rol:
        return False
    permisos = roles.get(rol, set())
    # EL OPERADOR CLAVE: <= (is subset)
    # Devuelve True solo si el usuario tiene TODOS los permisos que pide la acción.
    return acciones_requeridas <= permisos  # subconjunto

verificaciones = [
    ("Juan", {"leer", "eliminar"}),
    ("María", {"leer", "escribir"}),
    ("María", {"eliminar"}),
    ("Pedro", {"leer"}),
    ("Pedro", {"escribir"}),
    ("Ana", {"leer", "ver_logs"}),
]

for usuario, acciones in verificaciones:
    resultado = "✓" if puede_hacer(usuario, acciones) else "✗"
    print(f"  {resultado} {usuario} → {acciones}")


# 2. PERMISOS COMUNES (Intersección &)
# Sirve para auditoría: "¿Qué cosas pueden hacer tanto un editor como un moderador?"
# Ayuda a encontrar redundancias en la empresa.
print("\n" + "=" * 60)
print("2. PERMISOS COMUNES")
print("=" * 60)

pares_roles = [
    ("editor", "moderador"),
    ("moderador", "auditor"),
    ("editor", "auditor"),
]

for r1, r2 in pares_roles:
    comunes = roles[r1] & roles[r2]
    print(f"  {r1} ∩ {r2}: {sorted(comunes)}")


# 3. PERMISOS EXCLUSIVOS (Diferencia - y Unión |)
# Aquí la lógica es más avanzada:
# 1. 'otros_permisos' acumula la UNIÓN (|) de todos los roles menos el actual.
# 2. 'exclusivos' es la RESTA (-) de mis permisos menos todos los demás.
# Uso: Saber exactamente qué hace especial a un rol (ej: solo el Admin puede 'configurar').
print("\n" + "=" * 60)
print("3. PERMISOS EXCLUSIVOS")
print("=" * 60)

for nombre, permisos in roles.items():
    otros_permisos = set()
    for otro_nombre, otros in roles.items():
        if otro_nombre != nombre:
            otros_permisos = otros_permisos | otros # Acumula todo lo ajeno
    exclusivos = permisos - otros_permisos # Mi diferencia única
    if exclusivos:
        print(f"  {nombre}: {sorted(exclusivos)}")
    else:
        print(f"  {nombre}: (ninguno exclusivo)")


# 4. JERARQUÍA DE ROLES (Comparación de Superconjuntos >)
# Si el conjunto A tiene todos los elementos de B y además tiene más, 
# entonces A es un "Superconjunto" de B.
# Uso: Determinar quién manda sobre quién en el sistema.
print("\n" + "=" * 60)
print("4. JERARQUÍA DE ROLES")
print("=" * 60)

for r1 in roles:
    for r2 in roles:
        if r1 != r2 and roles[r2] < roles[r1]:
            print(f"  {r1} contiene todos los permisos de {r2}")


# 5. CREAR ROL COMBINADO (Unión |) e INTERSECCIÓN DE SEGURIDAD (&)
# Unimos dos roles para crear uno nuevo (ej: Editor + Auditor).
print("\n" + "=" * 60)
print("5. CREAR ROL COMBINADO")
print("=" * 60)

nuevo_rol = roles["editor"] | roles["auditor"]
print(f"  editor + auditor = {sorted(nuevo_rol)}")

# Verificar que no tenga permisos peligrosos
permisos_peligrosos = {"eliminar", "crear_usuarios", "configurar"}
conflictos = nuevo_rol & permisos_peligrosos
if conflictos:
    print(f"  Alerta: tiene permisos peligrosos: {conflictos}")
else:
    print(f"  Sin permisos peligrosos")