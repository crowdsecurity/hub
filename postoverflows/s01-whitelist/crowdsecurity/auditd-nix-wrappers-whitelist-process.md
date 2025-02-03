# Nix wrappers whitelist process

With the Nix package manager, certain executables are wrapped, meaning the executable in `PATH` is just a symlink to an executable named in the following way `/nix/store/<hash>/bin/.<program>-wrapped`. This will trigger the suspicious process detection because the name of the binary starts with a `.` character.

This postoverflow will whitelist processes that follow the `.<program>-wrapped` pattern if they are executed from `/nix/store`.
