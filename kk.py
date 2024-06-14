def fcfs(sectores, inicio):
    # FCFS: First-Come, First-Served
    orden_peticiones = sectores
    movimientos = sum(abs(orden_peticiones[i] - orden_peticiones[i - 1]) for i in range(1, len(sectores)))
    return orden_peticiones, movimientos

def sstf(sectores, inicio):
    # SSTF: Shortest Seek Time First
    orden_peticiones = []
    movimientos = 0
    while sectores:
        siguiente_sector = min(sectores, key=lambda x: abs(x - inicio))
        movimientos += abs(siguiente_sector - inicio)
        inicio = siguiente_sector
        orden_peticiones.append(siguiente_sector)
        sectores.remove(siguiente_sector)
    return orden_peticiones, movimientos

def scan(sectores, inicio):
    # SCAN: Elevador
    orden_peticiones = []
    movimientos = 0
    sectores.sort()
    while sectores:
        for sector in sectores[:]:
            if inicio <= sector:
                orden_peticiones.append(sector)
                movimientos += abs(sector - inicio)
                inicio = sector
                sectores.remove(sector)
        if sectores:
            inicio = max(sectores)
            orden_peticiones.append(inicio)
            movimientos += max(sectores) - inicio
            inicio = max(sectores)
            sectores.remove(inicio)
    return orden_peticiones, movimientos

def c_scan(sectores, inicio):
    # C-SCAN: Exploración Circular
    orden_peticiones = []
    movimientos = 0
    sectores.sort()
    while sectores:
        for sector in sectores[:]:
            if inicio <= sector:
                orden_peticiones.append(sector)
                movimientos += abs(sector - inicio)
                inicio = sector
                sectores.remove(sector)
        if sectores:
            inicio = min(sectores)
            orden_peticiones.append(inicio)
            movimientos += inicio - min(sectores)
            inicio = min(sectores)
            sectores.remove(inicio)
    return orden_peticiones, movimientos

# Ejemplo de uso:
sectores = [10,50, 80, 100, 120, 200,250]
inicio = 75  # Supongamos que el inicio es 75
metodo = 0  # Cambia el método según tus necesidades

if metodo == 0:
    orden, movimientos = fcfs(sectores, inicio)
elif metodo == 1:
    orden, movimientos = sstf(sectores, inicio)
elif metodo == 2:
    orden, movimientos = scan(sectores, inicio)
elif metodo == 3:
    orden, movimientos = c_scan(sectores, inicio)

print(f"Orden de peticiones: {orden}")
print(f"Total de movimientos entre sectores: {movimientos}")