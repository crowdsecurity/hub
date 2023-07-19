## nvm whitelist process

Since node version manager keep `node` and `npm` within a directory `.nvm` in the user's home directory, it will trigger our suspicious process detection. This postoverflow will whitelist the process `node` when they are executed from the `.nvm` directory.

This postoverflow is not supplied by default with auditd collection as you may not use nvm.