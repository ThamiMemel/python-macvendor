### Features

- Validate MAC Address / OUI (patterns are bellow)
- Get the manufactor of af a single or multiple MAC address/OUI
- Import it in your script/program or use it as CLI program

# python-macvendor
## Installation
`pip install macvendor`
## Basic Usage
### As CLI program
`$ macvendor.py -a 30:8d:99:15:c8:9A  00:01:42`
>| Mac               | Vendor             |
>|-------------------|--------------------|
>| 30:8d:99:15:c8:9A | Hewlett Packard    |
>| 00-01-52-55-33-34 | Chromatek Inc.     |
>| 00:01:42          | Cisco Systems, Inc |

### As liberary
```python
from macvendor import getVendor

print(getVendor("30:8d:99:15:c8:9A"))
```
> ['30:8d:99:15:c8:9A', 'Hewlett Packard']

```python
from macvendor import getVendorList

print(getVendorList(["30:8d:99:15:c8:9A", "00:01:42", "00-01-52-55-33-34"]))
```
>{'30:8d:99:15:c8:9A': 'Hewlett Packard', '00:01:42': 'Cisco Systems, Inc', '00-01-52-55-33-34': 'Chromatek Inc.'}


## 3d party Dependencies
##### Usage as liberary
No Dependencies
##### Usage in command line
Tabulate 0.8.6
## MAC / OUI accepted formats
*note: all patternes are case insensetive*
> XX:XX:XX:XX:XX:XX  
> XX-XX-XX-XX-XX-XX  
> XX.XX.XX.XX.XX.XX  
> XXXXXXXXXXXX  
> XX:XX:XX:FF:FE:XX:XX:XX  
> XX-XX-XX-FF-FE-XX-XX-XX  
> XX.XX.XX.FF.FE.XX.XX.XX  
> XXXXXXFFFEXXXXXX  
> XXX:XXX:XXX:XXX  
> XXX-XXX-XXX-XXX  
> XXX.XXX.XXX.XXX  
> XXXX:XXFF:FEXX:XXXX  
> XXXX-XXFF-FEXX-XXXX  
> XXXX.XXFF.FEXX.XXXX  
