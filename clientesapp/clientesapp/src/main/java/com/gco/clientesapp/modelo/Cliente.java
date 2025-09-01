package com.gco.clientesapp.modelo;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "cliente")
public class Cliente {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "tipo_identificacion")
    private String tipoIdentificacion;

    @Column(name = "numero_identificacion")
    private String numeroIdentificacion;

    private String nombres;
    private String apellidos;

    @Column(name = "fecha_nacimiento")
    private LocalDate fechaNacimiento;

    private String direccion;

    @Column(name = "id_ciudad")
    private Long idCiudad;

    @Column(name = "id_marca")
    private Long idMarca;

    public Cliente() {
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getTipoIdentificacion() { return tipoIdentificacion; }
    public void setTipoIdentificacion(String tipoIdentificacion) { this.tipoIdentificacion = tipoIdentificacion; }

    public String getNumeroIdentificacion() { return numeroIdentificacion; }
    public void setNumeroIdentificacion(String numeroIdentificacion) { this.numeroIdentificacion = numeroIdentificacion; }

    public String getNombres() { return nombres; }
    public void setNombres(String nombres) { this.nombres = nombres; }

    public String getApellidos() { return apellidos; }
    public void setApellidos(String apellidos) { this.apellidos = apellidos; }

    public LocalDate getFechaNacimiento() { return fechaNacimiento; }
    public void setFechaNacimiento(LocalDate fechaNacimiento) { this.fechaNacimiento = fechaNacimiento; }

    public String getDireccion() { return direccion; }
    public void setDireccion(String direccion) { this.direccion = direccion; }

    public Long getIdCiudad() { return idCiudad; }
    public void setIdCiudad(Long idCiudad) { this.idCiudad = idCiudad; }

    public Long getIdMarca() { return idMarca; }
    public void setIdMarca(Long idMarca) { this.idMarca = idMarca; }
}
