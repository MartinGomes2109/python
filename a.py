a = [1,2,3]
print(len(a))
b = []
print(a)
print(b)
c= a[0]
a.remove(a[0])
b.append(c)
print(a)
print(b)

                    if listo_susp:
                        if len(listo_susp) > 1:
                            proceso_susp = listo_susp[0]  # Verifica el primer proceso sin eliminarlo
                            if gestor_memoria.asignar_memoria(proceso_susp):
                                listo_susp.popleft()  # Solo elimina el proceso si se puede asignar memoria
                                self.agregar_proceso(proceso_susp)
                        else:
                            proceso_susp = listo_susp[0]  # Verifica el primer proceso sin eliminarlo
                            listo_susp.popleft() 
                            if gestor_memoria.asignar_memoria(proceso_susp):
                                # Solo elimina el proceso si se puede asignar memoria
                                self.agregar_proceso(proceso_susp)