# Forge Python Scripts

A collection of Forge Python scripts, currently with a count of one.


## py_forge_formats.py

Implements a Python wrapper around two basic Forge web service calls:

- Authenticate an app.
- Query the file formats currently supported by the translation processes.

Here is the result of running this script at the time of writing:

```
$ ./py_forge_formats.py
9 Forge output formats:
  dwg: f2d, f3d, rvt
  fbx: f3d
  ifc: rvt
  iges: f3d, fbx, iam, ipt, wire
  obj: asm, f3d, fbx, iam, ipt, neu, prt, sldasm, sldprt, step, stp, stpz,
    wire, x_b, x_t, asm.NNN, neu.NNN, prt.NNN
  step: f3d, fbx, iam, ipt, wire
  stl: f3d, fbx, iam, ipt, wire
  svf: 3dm, 3ds, asm, catpart, catproduct, cgr, collaboration, dae, dgn,
    dlv3, dwf, dwfx, dwg, dwt, dxf, exp, f3d, fbx, g, gbxml, iam, idw,
    ifc, ige, iges, igs, ipt, jt, max, model, neu, nwc, nwd, obj, pdf,
    prt, rcp, rvt, sab, sat, session, skp, sldasm, sldprt, smb, smt,
    ste, step, stl, stla, stlb, stp, stpz, wire, x_b, x_t, xas, xpr,
    zip, asm.NNN, neu.NNN, prt.NNN
  thumbnail: 3dm, 3ds, asm, catpart, catproduct, cgr, collaboration, dae, dgn,
    dlv3, dwf, dwfx, dwg, dwt, dxf, exp, f3d, fbx, g, gbxml, iam, idw,
    ifc, ige, iges, igs, ipt, jt, max, model, neu, nwc, nwd, obj, pdf,
    prt, rcp, rvt, sab, sat, session, skp, sldasm, sldprt, smb, smt,
    ste, step, stl, stla, stlb, stp, stpz, wire, x_b, x_t, xas, xpr,
    zip, asm.NNN, neu.NNN, prt.NNN
```

This script replaces and improves on the previous `forgeauth` and `forgeformats` Unix shell cURL scripts documented in the discussion of
the [`cURL` wrapper scripts to list Forge file formats](http://thebuildingcoder.typepad.com/blog/2016/10/forge-intro-formats-webinars-and-fusion-360-client-api.html#3).

For the sake of completeness, those two scripts have been added to this repository as well.


## Setup and Usage

Before you can make any use of the Forge web services, you will need to register an app and request the API client id and client secret for it
at [developer.autodesk.com](https://developer.autodesk.com)
&gt; [my apps](https://developer.autodesk.com/myapps).

These scripts assume that you have stored these creadentials in the environment variables `FORGE_CLIENT_ID` and `FORGE_CLIENT_SECRET`.


## <a name="98"></a>Author

Jeremy Tammik,
[The Building Coder](http://thebuildingcoder.typepad.com) and
[The 3D Web Coder](http://the3dwebcoder.typepad.com),
[ADN](http://www.autodesk.com/adn)
[Open](http://www.autodesk.com/adnopen),
[Forge Partner Development](http://forge.autodesk.com),
[Autodesk Inc.](http://www.autodesk.com)


## <a name="99"></a>License

This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT).
Please see the [LICENSE](LICENSE) file for full details.

