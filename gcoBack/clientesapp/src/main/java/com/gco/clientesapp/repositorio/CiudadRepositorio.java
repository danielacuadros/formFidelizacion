    // CiudadRepositorio.java
    package com.gco.clientesapp.repositorio;

    import com.gco.clientesapp.modelo.Ciudad;
    import org.springframework.data.jpa.repository.JpaRepository;
    import org.springframework.data.jpa.repository.Query;
    import org.springframework.stereotype.Repository;
    import java.util.List;

    @Repository
    public interface CiudadRepositorio extends JpaRepository<Ciudad, Long> {

        // Buscar ciudades por país
        List<Ciudad> findByPaisOrderByNombreCiudad(String pais);

        // Buscar ciudades por departamento
        List<Ciudad> findByDepartamentoOrderByNombreCiudad(String departamento);

        // Obtener todos los países únicos
        @Query("SELECT DISTINCT c.pais FROM Ciudad c ORDER BY c.pais")
        List<String> findDistinctPaises();

        // Obtener departamentos por país
        @Query("SELECT DISTINCT c.departamento FROM Ciudad c WHERE c.pais = ?1 ORDER BY c.departamento")
        List<String> findDepartamentosByPais(String pais);
    }