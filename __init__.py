# ----------------------------------------------------------
# File __init__.py
# ----------------------------------------------------------

#    Addon info
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
#  as published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

# Please check the LICENSE file for the full license
#
#  You should have received a copy of the GNU General Public License Version 3, 29 June 2007
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
##############################################################################################
#In addition to the GPL license, the following terms apply to all files in the "bdental_3_modules" folder:
#This program use the following modules:
#vtk :
# /*=========================================================================

#   Program:   Visualization Toolkit
#   Module:    Copyright.txt

# Copyright (c) 1993-2015 Ken Martin, Will Schroeder, Bill Lorensen
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.

#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

#  * Neither name of Ken Martin, Will Schroeder, or Bill Lorensen nor the names
#    of any contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# =========================================================================*/
#
# SimpleITK & OpenCV :
# Apache License
#                            Version 2.0, January 2004
#                         http://www.apache.org/licenses/

#    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

#    1. Definitions.

#       "License" shall mean the terms and conditions for use, reproduction,
#       and distribution as defined by Sections 1 through 9 of this document.

#       "Licensor" shall mean the copyright owner or entity authorized by
#       the copyright owner that is granting the License.

#       "Legal Entity" shall mean the union of the acting entity and all
#       other entities that control, are controlled by, or are under common
#       control with that entity. For the purposes of this definition,
#       "control" means (i) the power, direct or indirect, to cause the
#       direction or management of such entity, whether by contract or
#       otherwise, or (ii) ownership of fifty percent (50%) or more of the
#       outstanding shares, or (iii) beneficial ownership of such entity.

#       "You" (or "Your") shall mean an individual or Legal Entity
#       exercising permissions granted by this License.

#       "Source" form shall mean the preferred form for making modifications,
#       including but not limited to software source code, documentation
#       source, and configuration files.

#       "Object" form shall mean any form resulting from mechanical
#       transformation or translation of a Source form, including but
#       not limited to compiled object code, generated documentation,
#       and conversions to other media types.

#       "Work" shall mean the work of authorship, whether in Source or
#       Object form, made available under the License, as indicated by a
#       copyright notice that is included in or attached to the work
#       (an example is provided in the Appendix below).

#       "Derivative Works" shall mean any work, whether in Source or Object
#       form, that is based on (or derived from) the Work and for which the
#       editorial revisions, annotations, elaborations, or other modifications
#       represent, as a whole, an original work of authorship. For the purposes
#       of this License, Derivative Works shall not include works that remain
#       separable from, or merely link (or bind by name) to the interfaces of,
#       the Work and Derivative Works thereof.

#       "Contribution" shall mean any work of authorship, including
#       the original version of the Work and any modifications or additions
#       to that Work or Derivative Works thereof, that is intentionally
#       submitted to Licensor for inclusion in the Work by the copyright owner
#       or by an individual or Legal Entity authorized to submit on behalf of
#       the copyright owner. For the purposes of this definition, "submitted"
#       means any form of electronic, verbal, or written communication sent
#       to the Licensor or its representatives, including but not limited to
#       communication on electronic mailing lists, source code control systems,
#       and issue tracking systems that are managed by, or on behalf of, the
#       Licensor for the purpose of discussing and improving the Work, but
#       excluding communication that is conspicuously marked or otherwise
#       designated in writing by the copyright owner as "Not a Contribution."

#       "Contributor" shall mean Licensor and any individual or Legal Entity
#       on behalf of whom a Contribution has been received by Licensor and
#       subsequently incorporated within the Work.

#    2. Grant of Copyright License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       copyright license to reproduce, prepare Derivative Works of,
#       publicly display, publicly perform, sublicense, and distribute the
#       Work and such Derivative Works in Source or Object form.

#    3. Grant of Patent License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       (except as stated in this section) patent license to make, have made,
#       use, offer to sell, sell, import, and otherwise transfer the Work,
#       where such license applies only to those patent claims licensable
#       by such Contributor that are necessarily infringed by their
#       Contribution(s) alone or by combination of their Contribution(s)
#       with the Work to which such Contribution(s) was submitted. If You
#       institute patent litigation against any entity (including a
#       cross-claim or counterclaim in a lawsuit) alleging that the Work
#       or a Contribution incorporated within the Work constitutes direct
#       or contributory patent infringement, then any patent licenses
#       granted to You under this License for that Work shall terminate
#       as of the date such litigation is filed.

#    4. Redistribution. You may reproduce and distribute copies of the
#       Work or Derivative Works thereof in any medium, with or without
#       modifications, and in Source or Object form, provided that You
#       meet the following conditions:

#       (a) You must give any other recipients of the Work or
#           Derivative Works a copy of this License; and

#       (b) You must cause any modified files to carry prominent notices
#           stating that You changed the files; and

#       (c) You must retain, in the Source form of any Derivative Works
#           that You distribute, all copyright, patent, trademark, and
#           attribution notices from the Source form of the Work,
#           excluding those notices that do not pertain to any part of
#           the Derivative Works; and

#       (d) If the Work includes a "NOTICE" text file as part of its
#           distribution, then any Derivative Works that You distribute must
#           include a readable copy of the attribution notices contained
#           within such NOTICE file, excluding those notices that do not
#           pertain to any part of the Derivative Works, in at least one
#           of the following places: within a NOTICE text file distributed
#           as part of the Derivative Works; within the Source form or
#           documentation, if provided along with the Derivative Works; or,
#           within a display generated by the Derivative Works, if and
#           wherever such third-party notices normally appear. The contents
#           of the NOTICE file are for informational purposes only and
#           do not modify the License. You may add Your own attribution
#           notices within Derivative Works that You distribute, alongside
#           or as an addendum to the NOTICE text from the Work, provided
#           that such additional attribution notices cannot be construed
#           as modifying the License.

#       You may add Your own copyright statement to Your modifications and
#       may provide additional or different license terms and conditions
#       for use, reproduction, or distribution of Your modifications, or
#       for any such Derivative Works as a whole, provided Your use,
#       reproduction, and distribution of the Work otherwise complies with
#       the conditions stated in this License.

#    5. Submission of Contributions. Unless You explicitly state otherwise,
#       any Contribution intentionally submitted for inclusion in the Work
#       by You to the Licensor shall be under the terms and conditions of
#       this License, without any additional terms or conditions.
#       Notwithstanding the above, nothing herein shall supersede or modify
#       the terms of any separate license agreement you may have executed
#       with Licensor regarding such Contributions.

#    6. Trademarks. This License does not grant permission to use the trade
#       names, trademarks, service marks, or product names of the Licensor,
#       except as required for reasonable and customary use in describing the
#       origin of the Work and reproducing the content of the NOTICE file.

#    7. Disclaimer of Warranty. Unless required by applicable law or
#       agreed to in writing, Licensor provides the Work (and each
#       Contributor provides its Contributions) on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#       implied, including, without limitation, any warranties or conditions
#       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
#       PARTICULAR PURPOSE. You are solely responsible for determining the
#       appropriateness of using or redistributing the Work and assume any
#       risks associated with Your exercise of permissions under this License.

#    8. Limitation of Liability. In no event and under no legal theory,
#       whether in tort (including negligence), contract, or otherwise,
#       unless required by applicable law (such as deliberate and grossly
#       negligent acts) or agreed to in writing, shall any Contributor be
#       liable to You for damages, including any direct, indirect, special,
#       incidental, or consequential damages of any character arising as a
#       result of this License or out of the use or inability to use the
#       Work (including but not limited to damages for loss of goodwill,
#       work stoppage, computer failure or malfunction, or any and all
#       other commercial damages or losses), even if such Contributor
#       has been advised of the possibility of such damages.

#    9. Accepting Warranty or Additional Liability. While redistributing
#       the Work or Derivative Works thereof, You may choose to offer,
#       and charge a fee for, acceptance of support, warranty, indemnity,
#       or other liability obligations and/or rights consistent with this
#       License. However, in accepting such obligations, You may act only
#       on Your own behalf and on Your sole responsibility, not on behalf
#       of any other Contributor, and only if You agree to indemnify,
#       defend, and hold each Contributor harmless for any liability
#       incurred by, or claims asserted against, such Contributor by reason
#       of your accepting any such warranty or additional liability.

#    END OF TERMS AND CONDITIONS

#    APPENDIX: How to apply the Apache License to your work.

#       To apply the Apache License to your work, attach the following
#       boilerplate notice, with the fields enclosed by brackets "[]"
#       replaced with your own identifying information. (Don't include
#       the brackets!)  The text should be enclosed in the appropriate
#       comment syntax for the file format. We also recommend that a
#       file or class name and description of purpose be included on the
#       same "printed page" as the copyright notice for easier
#       identification within third-party archives.

#    Copyright [yyyy] [name of copyright owner]

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
bl_info = {
    "name": "Bdental-3",  
    "author": "Dr. Essaid Issam Dakir DMD\n,Dr. Ilya Fomenco DMD\n, Dr. Krasouski Dmitry DMD",
    "version": (4, 2, 0),
    "blender": (4, 2, 0),  
    "location": "3D View -> UI SIDE PANEL ",
    "description": "3D Digital Dentistry",  
    "warning": "",
    "doc_url": "",
    "tracker_url": "https://t.me/bdental3",
    "category": "Dental",  
}
#############################################################################################
# IMPORTS :
#############################################################################################
# Python imports :

import sys
import shutil
import os
import bpy
import zipfile
import socket
import webbrowser
from importlib import import_module
from os.path import dirname,basename, join, abspath, expanduser,exists, isfile, isdir
from time import sleep
import threading
import gpu
from gpu_extras.batch import batch_for_shader
import blf
import tempfile
from glob import glob
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(
        encoding="cp65001"
    )  # activate unicode characters in windows CLI


BLF_INFO = {
    "fontid" : 0,
    "size" : 18
}
class BdentalColors():
    white = [0.8,0.8,0.8,1.0]
    black = [0.0,0.0,0.0,1.0]
    trans = [0.8,0.8,0.8,0.0]
    red = [1.0,0.0,0.0,1.0]
    orange = [0.8, 0.258385, 0.041926, 1.0]
    yellow = [0.4,0.4,0.1,1]
    green = [0,1,0.2,0.7]
    blue = [0.2,0.1,1,0.2]
    default = orange





DRAW_HANDLERS = []
REPO_URL = "https://github.com/issamdakir/Bdental-3-win/zipball/main"
VERSION_URL = "https://raw.githubusercontent.com/issamdakir/Bdental-3-win/main/Resources/BDENTAL_Version.txt"
ADDON_UPDATE_URL = "https://github.com/issamdakir/Bdental-3-update/zipball/main"
UPDATE_VERSION_URL = "https://raw.githubusercontent.com/issamdakir/Bdental-3-update/main/data/BDENTAL_Version.txt"
GITHUB_CMD = "curl -L https://github.com/issamdakir/Bdental-3-win/zipball/main"
TELEGRAM_LINK = "https://t.me/bdental3"
REQ_DICT = {
    "SimpleITK": "SimpleITK",
    "vtk": "vtk",
    "cv2.aruco": "opencv-contrib-python",
}
ERROR_PANEL = False
ERROR_MESSAGE = []
ADDON_DIR = dirname(abspath(__file__))
RESOURCES = join(ADDON_DIR, "Resources")
BDENTAL_LIBRARY_PATH = join(RESOURCES, "Bdental_Library")
# user_lib = bpy.context.preferences.filepaths.asset_libraries.get('Bdental Library')
# if user_lib :
#     user_lib.path = BDENTAL_LIBRARY_PATH
ADDON_VER_PATH = join(RESOURCES, "BDENTAL_Version.txt")
ADDON_VER_DATE = "  "

if exists(ADDON_VER_PATH):
    with open(ADDON_VER_PATH, "r") as rf:
        lines = rf.readlines()
        ADDON_VER_DATE = lines[0].split(";")[0]

BDENTAL_MODULES = join(ADDON_DIR, "bdental_modules")
sys.path.insert(0,BDENTAL_MODULES)
# BDENTAL_MODULES_ZIP = join(RESOURCES, "bdental_modules.zip")
#############################################################
def bdental_log(txt_list,header=None,footer=None):
    _header, _footer = header, footer
    if _header is None :
        _header=f"\n{'#'*20} Bdental log :  {'#'*20}\n"
    if _footer is None:
        _footer=f"\n{'#'*20} End log.\  {'#'*20}\n"
    
    print(_header)
    for line in txt_list :
        print(line)
    print(_footer)
def add_bdental_libray():
    if not exists(BDENTAL_LIBRARY_PATH) :
        os.mkdir(BDENTAL_LIBRARY_PATH)
    lib_archive_dir_path = join(BDENTAL_LIBRARY_PATH, "lib_archive")
    if exists(lib_archive_dir_path) :
        files = glob(join(lib_archive_dir_path, "*"))
        
        for f in files :
            if f.endswith(".zip"):
                with zipfile.ZipFile(f, 'r') as zip_ref:
                    zip_ref.extractall(BDENTAL_LIBRARY_PATH)
            else:
                dst = join(BDENTAL_LIBRARY_PATH, basename(f))
                if exists(dst):
                    os.remove(dst)

                shutil.move(f, BDENTAL_LIBRARY_PATH)
        shutil.rmtree(lib_archive_dir_path)

    user_lib = bpy.context.preferences.filepaths.asset_libraries.get('Bdental Library') 
    
    if user_lib :
        user_lib.path = BDENTAL_LIBRARY_PATH
    else :
        bpy.ops.preferences.asset_library_add(directory=BDENTAL_LIBRARY_PATH)

    return
def ImportReq(REQ_DICT):
    Pkgs = []
    for mod, pkg in REQ_DICT.items():
        try:
            import_module(mod)
        except ImportError:
            Pkgs.append(pkg)

    return Pkgs

def isConnected():
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        return False

def browse(url) :
    success = 0
    try :
        webbrowser.open(url)
        success = 1
        return success
    except Exception as er :
        print(f"open telegram link error :\n{er}")
        return success

def start_blender_session():
    # print(f"binary path : {bpy.app.binary_path}")
    os.system(f'"{bpy.app.binary_path}"')

# def addon_update(_dir, addon_dir):
     
#     for elmt in os.listdir(_dir):
#         fullpath = join(addon_dir,elmt)
#         new_elmt = join(_dir,elmt)
#         if exists(fullpath) :
#             if isfile(fullpath) :
#                 os.remove(fullpath)
#                 shutil.move(new_elmt, addon_dir)
#             else :
#                 if not "bdental_modules" in elmt.lower() :
#                     shutil.rmtree(fullpath)
#                     shutil.move(new_elmt, addon_dir)
#                 else :
#                     resources = join(addon_dir, "Resources")
#                     shutil.move(new_elmt, resources)

def exit_blender():
    sys.exit(0)

def gpu_info_footer(rect_color, text_list, button=False, btn_txt="", pourcentage=100):
    global BLF_INFO
    if pourcentage <= 0:
        pourcentage = 1
    if pourcentage > 100:
        pourcentage = 100

    def draw_callback_function():

        w = int(bpy.context.area.width * (pourcentage/100))
        for i, txt in enumerate((reversed(text_list))):

            h = 30
            # color = [0.4, 0.4, 0.8, 1.000000]
            # color =[0.9, 0.5, 0.000000, 1.000000]
            draw_gpu_rect(0, h*i, w, h, rect_color)
            blf.position(0, 10, 10 + (h*i), 0)
            blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
            r, g, b, a = (0.0, 0.0, 0.0, 1.0)
            blf.color(0, r, g, b, a)
            blf.draw(0, txt)

        if button:

            h = 30
            color = [0.8, 0.258385, 0.041926, 1.0]
            draw_gpu_rect(w-110, 2, 100, h-4, color)
            blf.position(0, w-85, 10, 0)
            blf.size(BLF_INFO.get("fontid"), BLF_INFO.get("size")) # 3.6 api blf.size(0, 40, 30) -> blf.size(fontid, size)
            r, g, b, a = (0.0, 0.0, 0.0, 1.0)
            blf.color(0, r, g, b, a)
            blf.draw(0, btn_txt)

    info_handler = bpy.types.SpaceView3D.draw_handler_add(
        draw_callback_function, (), "WINDOW", "POST_PIXEL"
    )
    # redraw scene
    # bpy.ops.wm.redraw_timer(type = 'DRAW_WIN_SWAP', iterations = 1)
    # for area in bpy.context.window.screen.areas:
    #     if area.type == "VIEW_3D":
    #         area.tag_redraw()

    return info_handler

def get_btn_bb(btn_index=0, btn_width=100, btn_height=26, padding_x=10, padding_y=2, safe_area=5):
    area3d = None
    area3d_check = [
        area for area in bpy.context.screen.areas if area.type == "VIEW_3D"]
    if area3d_check:
        area3d = area3d_check[0]
    if area3d:
        w = area3d.width
        x_min = w - padding_x - (btn_width*(btn_index+1)) - \
            (padding_x*btn_index) - safe_area
        x_max = w - padding_x - (btn_width*(btn_index)) - \
            (padding_x*btn_index) + safe_area
        y_min = 0
        y_max = btn_height+safe_area
        btn_bb = {
            "x_min": x_min,
            "x_max": x_max,
            "y_min": y_min,
            "y_max": y_max
        }
        return btn_bb
    else:
        return None

def draw_gpu_rect(x, y, w, h, rect_color):

    vertices = (
        (x, y), (x, y + h),
        (x + w, y + h), (x + w, y))

    indices = (
        (0, 1, 2), (0, 2, 3)
    )

    gpu.state.blend_set('ALPHA')
    shader = gpu.shader.from_builtin('UNIFORM_COLOR') # 3.6 api '2D_UNIFORM_COLOR'
    batch = batch_for_shader(
        shader, 'TRIS', {"pos": vertices}, indices=indices)
    shader.bind()
    shader.uniform_float("color", rect_color)
    batch.draw(shader)

def update_info(message=[], remove_handlers=True, button=False, btn_txt="", pourcentage=100, redraw_timer=True, rect_color=BdentalColors.default):
    global DRAW_HANDLERS

    if remove_handlers:
        for _h in DRAW_HANDLERS:
            bpy.types.SpaceView3D.draw_handler_remove(_h, "WINDOW")
        DRAW_HANDLERS = []
    if message:
        info_handler = gpu_info_footer(
            text_list=message, button=False, btn_txt="", pourcentage=100, rect_color=rect_color)
        DRAW_HANDLERS.append(info_handler)
    if redraw_timer:
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

def write_json(Dict,outPath) :
    jsonString = json.dumps(Dict,indent=4)
    with open(outPath, 'w') as wf :
        wf.write(jsonString)

def open_json(jsonPath) :
    with open(jsonPath, "r") as f:
        dataDict = json.load(f)
    return dataDict
# def addon_download():
#     global GITHUB_CMD

#     message = []
#     download_is_ok = False
#     _dir = None 

#     temp_dir = tempfile.mkdtemp()
#     os.chdir(temp_dir)
#     bdental_zip = join(temp_dir,'Bdental-3.zip')
#     _counter = 0
#     while _counter <= 3 :
#         _counter += 1
#         print(_counter)
#         os.system(f"{GITHUB_CMD} > {bdental_zip}")
#         if exists(bdental_zip) :
#             download_is_ok = True
#             print(f"number of url curls : {_counter} -> zip file downloaded : ", bdental_zip)
#             break
    
#     if not download_is_ok :
#         message.extend(["Error : curl bdental.zip download"])
#         return message,_dir

    
    
#     try :
#         with zipfile.ZipFile(bdental_zip, 'r') as zip_ref:
#             zip_ref.extractall(temp_dir)
#     except :
#         message.extend([f"Error : extract downloaded zip file {bdental_zip}"])
#         return message,_dir
#     src = [abspath(e) for e in os.listdir(temp_dir) if isdir(abspath(e))][0]
#     _dir = join(temp_dir,"Bdental-3")
#     os.rename(src,_dir)
#     return message,_dir

def addon_download():
    global REPO_URL
    message = []
    _dir = None 
    try :
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        bdental_zip_local = join(temp_dir,'Bdental-3.zip')

        # Download the file
        with requests.get(REPO_URL, stream=True, timeout=10) as r:
            try:
                r.raise_for_status()
            except HTTPError as http_err:
                txt = "HTTP error occurred"
                print(f"{txt} : {http_err}")
                message.extend([txt])
                return message,_dir
            except ConnectionError as conn_err:
                txt = "Connection error occurred"
                print(f"{txt} : {conn_err}")
                message.extend([txt])
                return message,_dir
            except Timeout as timeout_err:
                txt = "Timeout error occurred"
                print(f"{txt} : {timeout_err}")
                message.extend([txt])
                return message,_dir
            except RequestException as req_err:
                txt = f"Error during requests to {REPO_URL}"
                print(f"{txt} : {req_err}")
                message.extend([txt])
                return message,_dir
            
            with open(bdental_zip_local, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        
        
        try :
            with zipfile.ZipFile(bdental_zip_local, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
        except zipfile.BadZipFile as zip_err:
            txt = "Error occurred while extracting the downloaded addon ZIP file"
            print(f"{txt} : {zip_err}")
            message.extend([txt])
            return message,_dir
        
        src = [abspath(e) for e in os.listdir(temp_dir) if isdir(abspath(e))][0]
        _dir = join(temp_dir,"Bdental-3")
        os.rename(src,_dir)

    except OSError as os_err:
        print(f"OS error occurred: {os_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}") 
    return message,_dir

def addon_update_download():
    global ADDON_UPDATE_URL
    message = []
    update_root = None 
    try :
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        Bdental_3_update_zip_local = join(temp_dir,'Bdental_3_update.zip')

        # Download the file
        with requests.get(ADDON_UPDATE_URL, stream=True, timeout=10) as r:
            try:
                r.raise_for_status()
            except HTTPError as http_err:
                txt = "HTTP error occurred"
                bdental_log([f"{txt} : {http_err}"])
                message.extend([txt])
                return message,update_root
            except ConnectionError as conn_err:
                txt = "Connection error occurred"
                bdental_log([f"{txt} : {conn_err}"])
                message.extend([txt])
                return message,update_root
            except Timeout as timeout_err:
                txt = "Timeout error occurred"
                bdental_log([f"{txt} : {timeout_err}"])
                message.extend([txt])
                return message,update_root
            except RequestException as req_err:
                txt = f"Error during requests to {REPO_URL}"
                bdental_log([f"{txt} : {req_err}"])
                message.extend([txt])
                return message,update_root
            
            with open(Bdental_3_update_zip_local, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        
        
        try :
            with zipfile.ZipFile(Bdental_3_update_zip_local, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
        except zipfile.BadZipFile as zip_err:
            txt = "Error occurred while extracting the downloaded addon ZIP file"
            bdental_log([f"{txt} : {zip_err}"])
            message.extend([txt])
            return message,update_root
        
        src = [abspath(e) for e in os.listdir(temp_dir) if isdir(abspath(e))][0]
        update_root = join(temp_dir,"Bdental-3-update")
        os.rename(src,update_root)
        return message,update_root

    except OSError as os_err:
        bdental_log([f"OS error occurred: {os_err}"])
        message.extend([txt])
        return message,update_root
    except Exception as err:
        bdental_log([f"An unexpected error occurred: {err}"]) 
        message.extend([txt])
        return message,update_root

def addon_update_preinstall(update_root):
    global ADDON_DIR
    update_data_map_json = join(update_root, "update_data_map.json")
    update_data_map_dict = open_json(update_data_map_json)
    update_data_dir = join(update_root, "data")
    items = os.listdir(update_data_dir)
    # update_data_dict = {}
    # for i in items :
    #     k = join(update_data_dir,i)
    #     v = join(ADDON_DIR,*update_data_map_dict.get(i))
    update_data_dict = {join(update_data_dir,i) : join(ADDON_DIR,*update_data_map_dict.get(i)) for i in items}
    for src,dst in update_data_dict.items():
        if not "bdental_modules" in src.lower() :
            if exists(dst) :
                if isfile(dst) :
                    os.remove(dst)
                else :
                    shutil.rmtree(dst)
            else :
                if not exists(dirname(dst)) :
                    os.makedirs(dirname(dst))

            shutil.move(src, dirname(dst))
        else :
            resources = join(ADDON_DIR, "Resources")
            shutil.move(src, resources)

     
    

class BDENTAL_OT_SupportTelegram(bpy.types.Operator):
        """ open telegram bdental support link"""

        bl_idname = "wm.bdental_support_telegram"
        bl_label = "Bdental Support (Telegram)"

        #### this freezes blender ui !! ###
        # @classmethod
        # def poll(cls, context):
        #     return isConnected()
        ###################################


        def execute(self, context):
            global TELEGRAM_LINK
            browse(TELEGRAM_LINK)
            
            return{"FINISHED"}

class BdentalAddonPreferences(bpy.types.AddonPreferences):
        bl_idname = __name__

        def draw(self, context):
            layout = self.layout
            box = layout.box()
            row = box.row()
            row.operator("wm.bdental_add_app_template", text="Bdental as template",icon="SETTINGS")
            row = box.row()
            row.operator("wm.bdental_set_config", text="Bdental as default", icon="TOOL_SETTINGS")

class BDENTAL_OT_checkUpdate(bpy.types.Operator):
    """ check addon update """

    bl_idname = "wm.bdental_checkupdate"
    bl_label = "check update"
    bl_options = {"REGISTER", "UNDO"}

    txt = []
    restart = 0
    
    def modal(self, context, event):
        if not event.type in {'ESC', 'RET'}:
            return {'PASS_THROUGH'}

        elif event.type in {'ESC'}:
            update_info(["Bdental update Cancelled./"], rect_color=BdentalColors.red)
            sleep(1)
            update_info()
            return {'CANCELLED'}
        
        elif event.type in {'RET'} and event.value == "PRESS":
            global ADDON_DIR
            update_info(["Downloading..."])
            _message, update_root = addon_update_download()
            if _message :
                bdental_log(_message)
                update_info(message=_message, rect_color=BdentalColors.red)
                sleep(3)
                update_info()
                return{"CANCELLED"}
            
            update_info(message=["Preparing update..."])
            addon_update_preinstall(update_root)
            add_bdental_libray()
            update_info(["Please restart blender to finalize Bdental update."], rect_color=BdentalColors.green)
            # sleep(5)
            # update_info()
            
            return {'FINISHED'}
        return {'RUNNING_MODAL'}
        

    def invoke(self, context, event):
        if not isConnected() :
            update_info(message=["Bdental update : Please check internet connexion !"], rect_color=BdentalColors.red)
            sleep(3)
            update_info()
            return{"CANCELLED"}

        global ADDON_VER_PATH
        global UPDATE_VERSION_URL
        
        success = 0
        update_info(message=["Server connect..."])
        try :
            r = requests.get(UPDATE_VERSION_URL)
            success = r.ok
        except Exception as er :
            txt_list = [f"request github bdental version error : {er}"]
            bdental_log(txt_list)
            
        if not success :
            bdental_log([f"request response = {r.text}"])
            update_info(message=["Bdental update : server conexion error !"], rect_color=BdentalColors.red)
            sleep(3)
            update_info()
            return{"CANCELLED"}

        last_txt, last_num_txt = r.text.split(";")
        last_num = int(last_num_txt)
        current_txt = "unknown"
        txt_list = [f"Bdental addon update check : Current = {current_txt} Last release = {last_txt}"]
        
        if exists(ADDON_VER_PATH):
            with open(ADDON_VER_PATH, "r") as rf:
                lines = rf.readlines()
                current_txt, current_num = lines[0].split(";")
                current_num = int(current_num)
                
            txt_list = [f"Bdental addon update check : Current version = {current_txt} / Last version = {last_txt}"]
            
            
            if last_num <= current_num :
                txt_list = ["Bdental is up to date."]
                bdental_log(txt_list)
                update_info(message=txt_list, rect_color=BdentalColors.green)
                sleep(3)
                update_info()
                return{"CANCELLED"}

        update_info(message=txt_list+["<ENTER> : to install last update / <ESC> : to cancel"], rect_color=BdentalColors.yellow)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


class BDENTAL_PT_ModulesErrorPanel(bpy.types.Panel):
        """ Modules error panel"""

        bl_idname = "BDENTAL_PT_ModulesErrorPanel"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI" 
        bl_category = "BDENTAL"
        bl_label = f"BDENTAL (ver. {ADDON_VER_DATE})"

        def draw(self, context):

            layout = self.layout
            
            box = layout.box()
            grid = box.grid_flow(columns=1, align=True)
            grid.alert = True
            for l in ERROR_MESSAGE :
                grid.label(text=l)
            grid = box.grid_flow(columns=2, align=True)
            grid.operator("wm.bdental_checkupdate")
            grid.operator("wm.bdental_support_telegram")


###################################################
txt_list = [f"bdental version : {bl_info.get('version')}", f"bdental version date: {ADDON_VER_DATE}"]
bdental_log(txt_list)
# print(f"bdental version : {bl_info.get('version')}")
# print(f"bdental version date: {ADDON_VER_DATE}")

new_modules = join(RESOURCES, "bdental_modules")
if exists(new_modules) :
    sleep(3)
    if exists(BDENTAL_MODULES):
        shutil.rmtree(BDENTAL_MODULES)

    shutil.move(new_modules, ADDON_DIR)



if not exists(BDENTAL_MODULES) :
    ERROR_PANEL = True
    ERROR_MESSAGE.extend([
            "Bdental Modules are not installed properly",
            "Please update the addon or",
            "contact support",
        ])

if not ERROR_PANEL :
    
    NotFoundPkgs = ImportReq(REQ_DICT)
    if NotFoundPkgs :
        ERROR_PANEL = True
        ERROR_MESSAGE.extend([
            "Bdental Modules are not installed properly",
            "Please update the addon or",
            "contact support",
        ])

if ERROR_PANEL :
    addon_modules = []
    init_classes = [
            BDENTAL_OT_SupportTelegram,
            BDENTAL_OT_checkUpdate,
            BDENTAL_PT_ModulesErrorPanel,
        ]
    def register():
        
        for module in addon_modules:
            module.register()
        for cl in init_classes:
            bpy.utils.register_class(cl)

    def unregister():
        
        for cl in reversed(init_classes):
            bpy.utils.unregister_class(cl)
        for module in reversed(addon_modules):
            module.unregister()
else:
    
    from . import BDENTAL_Props, BDENTAL_Panel
    from .Operators import (
        BDENTAL_Operators, looptools
    )
    addon_modules = [
    BDENTAL_Props,
    BDENTAL_Panel,
    BDENTAL_Operators,
    looptools
    
    ]
    init_classes = [
        BDENTAL_OT_SupportTelegram,
        BdentalAddonPreferences,
        BDENTAL_OT_checkUpdate,
        ]

    def register():
        
        for module in addon_modules:
            module.register()
        for cl in init_classes:
            bpy.utils.register_class(cl)

    def unregister():
        for cl in reversed(init_classes):
            bpy.utils.unregister_class(cl)
        for module in reversed(addon_modules):
            module.unregister()
        

if __name__ == "__main__":
    register()