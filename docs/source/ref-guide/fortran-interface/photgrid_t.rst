.. _fortran-photgrid:

photgrid_t
~~~~~~~~~~

.. f:type:: photgrid_t

   The photgrid_t type represents a grid of photometric data.

   This grid may be used to interpolate the intensity (or related
   quantities) for a set of atmospheric parameter values.


   .. f:subroutine:: get_rank(rank)

      Get the rank (dimension) of the grid.

      :p integer rank [out]: Returned rank.


   .. f:subroutine:: get_axis(i, axis)

      Get an axis of the grid.

      :p integer i [in]: Index of axis (between 1 and `rank`)
      :p axis_t axis [out]: Returned axis.


   .. f:subroutine:: get_cache_count(cache_count)

      Get the number of nodes currently held in the grid cache.

      :p integer cache_count [out]: Returned number of nodes.

      
   .. f:subroutine:: get_cache_limit(cache_limit)

      Get the grid cache occupancy limit.

      :p integer cache_limit [out]: Returned occupancy limit.


   .. f:subroutine:: set_cache_limit(cache_limit, stat)

      Set the grid cache occupancy limit.

      :p integer cache_limit [in]: Occupancy limit.
      :o integer stat [out]: Status code.


   .. f:subroutine:: interp_intensity(x_vec, mu, I, stat, deriv_vec)

      Interpolate the photometric intensity, normalized to the zero-point flux.

      :p real(RD) x_vec(:) [in]: Atmospheric parameter values.
      :p real(RD) mu [in]: Cosine of angle of emergence relative to surface normal.
      :p real(RD) I [out]: Photometric intensity (/sr).
      :o integer stat [out]: Status code.
      :o logical deriv_vec(:) [in]: Derivative flags.

			 
   .. f:subroutine:: interp_E_moment(x_vec, k, E, stat, deriv_vec)

      Interpolate the photometric E-moment, normalized to the zero-point flux.

      :p real(RD) x_vec(:) [in]: Atmospheric parameter values.
      :p integer k [in]: Degree of of moment.
      :p real(RD) E [out]: Photometric E-moment.
      :o integer stat [out]: Status code.
      :o logical deriv_vec(:) [in]: Derivative flags.


   .. f:subroutine:: interp_D_moment(x_vec, l, D, stat, deriv_vec)

      Interpolate the photometric D-moment, normalized to the zero-point flux.

      :p real(RD) x_vec(:) [in]: Atmospheric parameter values.
      :p integer l [in]: Harmonic degree of moment.
      :p real(RD) D [out]: Photometric D-moment.
      :o integer stat [out]: Status code.
      :o logical deriv_vec(:) [in]: Derivative flags.


   .. f:subroutine:: interp_flux(x_vec, F, stat, deriv_vec)

      Interpolate the photometric flux, normalized to the zero-point flux.

      :p real(RD) x_vec(:) [in]: Atmospheric parameter values.
      :p real(RD) F [out]: Photometric flux.
      :o integer stat [out]: Status code.
      :o logical deriv_vec(:) [in]: Derivative flags.
