using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;

namespace Models.DTOs
{
    public class EspecialidadDto
    {

        public int Id { get; set; }

        [Required]
        [StringLength(60, MinimumLength = 1, ErrorMessage = "EL nombre debe ser Minimo 1 Maximo 60")]
        public string NombreEspecialidad { get; set; }
        [Required]
        [StringLength(100, MinimumLength = 1, ErrorMessage = "EL nombre debe ser Minimo 1 Maximo 100")]
        public string Descripcion { get; set; }

        public int Estado { get; set; }
    }
}
