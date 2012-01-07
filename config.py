# Copyright 2011 Ankur Goyal
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

settings_dict = {
    'url' : 'http://newyork.craigslist.org/aap/',
    'period' : 60,
    'neighborhoods' : [
        'east village', 
        'williamsburg', 
        'union square', 
        'bedford', 
    ],
    'badhoods' : [
        'bushwick',
        'bedford stuyvesant',
        'east williamsburg'
    ],
    'min_rent_person' : 1200,
    'max_rent_person' : 2000,
    'min_br' : 2,
    'max_br' : 3

}

class Settings(object):
    pass

settings = Settings()
for k,v in settings_dict.items():
    setattr(settings, k, v)
