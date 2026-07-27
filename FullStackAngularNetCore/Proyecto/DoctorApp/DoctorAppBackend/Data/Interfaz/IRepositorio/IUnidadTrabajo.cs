using System;
using System.Collections.Generic;
using System.Text;

namespace Data.Interfaz.IRepositorio
{
    public interface IUnidadTrabajo: IDisposable
    {
        IEspecialidadRepositorio Especialidad {  get; }

        Task Guardar();
    }
}
