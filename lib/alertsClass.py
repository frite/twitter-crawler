#!/usr/bin/env python
#
#   Copyright 2014 Frite M.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

#	Unicode codes came from blender
class textAlert:
    banner = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    failure = '\033[91m'
    endchar = '\033[0m'
    def header(self,message):
        print self.banner+message
    def okblue(self,message):
        print self.blue+message
    def okgreen(self,message):
        print self.green+message
    def warning(self,message):
        print self.warning+message
    def fail(self,message):
        print self.failure+message
    def endc(self,message):
        print self.endchar+message
