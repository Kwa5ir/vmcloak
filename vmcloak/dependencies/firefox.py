# Copyright (C) 2015-2018 Jurriaan Bremer.
# Copyright (C) 2018 Hatching B.V.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.
#
# See Archive
#https://archive.mozilla.org/pub/firefox/releases/
#

from vmcloak.abstract import Dependency

class Firefox(Dependency):
    name = "firefox"
    default = "115.0.0"
    tags = ["browser_firefox"]
    exes = [{
        "version": "41.0.2",
        "url": "https://cuckoo.sh/vmcloak/Firefox_Setup_41.0.2.exe",
        "sha1": "c5118ca76f0cf6ecda5d2b9292bf191525c9627a",
    }, {
        "version": "60.0.2",
        "url": "https://cuckoo.sh/vmcloak/firefox_60_0_2.exe",
        "sha1": "565c5ddca3e4acbc30a550f312d3a1a7fd8d8bce",
    }, {
        "version": "63.0.3",
        "url": "https://cuckoo.sh/vmcloak/firefox_63_0_3.exe",
        "sha1": "c5f03fc93aebd2db9da14ba6eb1f01e98e18d95b",
    }, {
        "version": "115.0.0",
        "url": "https://archive.mozilla.org/pub/firefox/releases/115.0esr/win64/en-US/Firefox%20Setup%20115.0esr.exe",
        "sha1": "cc304d56a5183f630cfe18b08376ba595bee6ce3",
    }  ]

    def run(self):
        self.upload_dependency("C:\\Firefox_Setup_41.0.2.exe")
        self.a.execute("C:\\Firefox_Setup_41.0.2.exe -ms")
        self.a.remove("C:\\Firefox_Setup_41.0.2.exe")

class Firefox41(Firefox, Dependency):
    """Backwards compatibility"""
    name = "firefox_41"
