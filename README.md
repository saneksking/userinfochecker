# User Info Checker <sup>v 0.0.2</sup>

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/saneksking/userinfochecker)](https://github.com/saneksking/userinfochecker/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/userinfochecker?label=pypi%20downloads)](https://pypi.org/project/userinfochecker/)
![GitHub top language](https://img.shields.io/github/languages/top/saneksking/userinfochecker)
[![PyPI](https://img.shields.io/pypi/v/userinfochecker)](https://pypi.org/project/userinfochecker)
[![GitHub](https://img.shields.io/github/license/saneksking/userinfochecker)](https://github.com/saneksking/userinfochecker/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/userinfochecker)](https://pypi.org/project/userinfochecker)
***
### User Info Checker - A library for get user information.
***

## Help:

---

`pip install userinfochecker`

```python
from user_info_checker import UserInfoChecker
from user_info_checker import SystemInfoChecker


user_info = UserInfoChecker()
system_info = SystemInfoChecker()
print(user_info.get_ip_address()) # Return IP address
print(user_info.get_hostname()) # Return hostname
print(user_info.get_city()) # Return city
print(user_info.get_region()) # Return region
print(user_info.get_country()) # Return country
print(user_info.get_loc()) # Return location
print(user_info.get_org()) # Return organisation
print(user_info.get_postal()) # Return postal
print(user_info.get_timezone()) # Return timezone
print(system_info.get_username()) # Return username

for k, v in user_info.data.items():
    print(f'{k}, {v}') # Return all info
```
***

## Disclaimer of liability:
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    ---------------------------------------------------------------------
