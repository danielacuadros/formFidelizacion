package com.gco.clientesapp.repositorio;

import com.gco.clientesapp.modelo.Marca;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MarcaRepositorio extends JpaRepository<Marca, Long> {

    // Buscar marca por nombre (Evita duplicados)
    Marca findByNombreMarcaIgnoreCase(String nombreMarca);
}
