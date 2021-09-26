--- setup.py.orig	2021-08-26 20:29:35 UTC
+++ setup.py
@@ -76,7 +76,7 @@ def invoke_make(**kwargs):
     subprocess.check_output("make -C src -f Makefile.vdf-client", shell=True)
 
 
-BUILD_VDF_CLIENT = os.getenv("BUILD_VDF_CLIENT", "Y") == "Y"
+BUILD_VDF_CLIENT = os.getenv("BUILD_VDF_CLIENT", "N") == "Y"
 BUILD_VDF_BENCH = os.getenv("BUILD_VDF_BENCH", "N") == "Y"
 
 
@@ -170,6 +170,7 @@ ext_modules = [
             get_pybind_include(),
             get_pybind_include(user=True),
             "mpir_gc_x64",
+            "/usr/local/include",
         ],
         library_dirs=["mpir_gc_x64"],
         libraries=["mpir"],
@@ -232,7 +233,8 @@ class BuildExt(build_ext):
         link_opts = self.l_opts.get(ct, [])
         if ct == "unix":
             opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
-            opts.append(cpp_flag(self.compiler))
+            opts.append('-DCMAKE_CXX_FLAGS=%s' % cpp_flag(self.compiler))
+            opts.append('-I/usr/local/include')
             if has_flag(self.compiler, "-fvisibility=hidden"):
                 opts.append("-fvisibility=hidden")
         elif ct == "msvc":
@@ -262,7 +264,6 @@ if platform.system() == "Windows":
     )
 else:
     build.sub_commands.append(("build_hook", lambda x: True))  # type: ignore
-    install.sub_commands.append(("install_hook", lambda x: True))
 
     setup(
         name="chiavdf",
@@ -274,11 +275,12 @@ else:
         long_description=open("README.md").read(),
         long_description_content_type="text/markdown",
         url="https://github.com/Chia-Network/chiavdf",
+        scripts=['tools/gen_pprods.py'],
         setup_requires=["pybind11>=2.5.0"],
-        ext_modules=[CMakeExtension("chiavdf", "src")],
-        cmdclass=dict(
-            build_ext=CMakeBuild, install_hook=install_hook, build_hook=build_hook
-        ),
+        ext_modules=ext_modules,
+        cmdclass={
+            "build_ext": BuildExt, "build_hook": build_hook
+        },
         zip_safe=False,
         use_scm_version={"fallback_version": "unknown-no-.git-directory"},
     )
