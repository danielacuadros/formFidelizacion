package com.gco.clientesapp.modelo;

import jakarta.persistence.*;

@Entity
@Table(name = "ciudades")
public class Ciudad {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_ciudad")
    private Long idCiudad;

    @Column(name = "nombre_ciudad", nullable = false, length = 100)
    private String nombreCiudad;

    @Column(name = "departamento", length = 100)
    private String departamento;

    @Column(name = "pais", length = 100)
    private String pais;

    public Ciudad() {
    }

    public Ciudad(String nombreCiudad, String departamento, String pais) {
        this.nombreCiudad = nombreCiudad;
        this.departamento = departamento;
        this.pais = pais;
    }

    public Long getIdCiudad() {
        return idCiudad;
    }

    public void setIdCiudad(Long idCiudad) {
        this.idCiudad = idCiudad;
    }

    public String getNombreCiudad() {
        return nombreCiudad;
    }

    public void setNombreCiudad(String nombreCiudad) {
        this.nombreCiudad = nombreCiudad;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    @Override
    public String toString() {
        return "Ciudad{" +
                "idCiudad=" + idCiudad +
                ", nombreCiudad='" + nombreCiudad + '\'' +
                ", departamento='" + departamento + '\'' +
                ", pais='" + pais + '\'' +
                '}';
    }
}
