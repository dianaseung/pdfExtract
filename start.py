#!/usr/bin/env python3
# Compiled one-step script to extract CVEs from a PDF and prepare them with markdown
from importlib import reload

import package.get_raw
import package.extract_cve
import package.markdown_cve


package = reload(package)

package.get_raw
package.extract_cve
package.markdown_cve