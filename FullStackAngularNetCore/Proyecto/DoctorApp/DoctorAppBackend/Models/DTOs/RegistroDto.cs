using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;

namespace Models.DTOs
{
    public class RegistroDto
    {
        [Required(ErrorMessage ="Username es Requerido")]
        public string Username { get; set; }
        [Required(ErrorMessage = "password es Requerida")]
        [StringLength(10, MinimumLength = 4,ErrorMessage ="El password debe debe de ser Minimo 4 Maximo 10 caracteres")]
        public string Password { get; set; }
    }
}
