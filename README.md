# PyMVG

A library to fetch MVG departure times of a given station by name from (old) HTML website.

(Currently not released to PyPI)

## Example

```python
import pymvg

station = 'Hauptbahnhof'
pymvg.get_departures_for(station)
```

See CLI example in `pymvg.py` file.

## License

See `LICENSE` file.