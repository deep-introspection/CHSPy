from ._chspy import (
		Anchor, CubicHermiteSpline, Extrema,
		interpolate, interpolate_vec, interpolate_diff, interpolate_diff_vec,
		extrema_from_anchors,
		norm_sq_interval, norm_sq_partial, scalar_product_interval, scalar_product_partial,
	)

try:
	from .version import version as __version__
except ImportError:
	from warnings import warn
	warn('Failed to find (autogenerated) version.py. Do not worry about this unless you really need to know the version.')
