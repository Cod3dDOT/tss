const execSync = require("child_process").execSync;

class MyError extends Error {
    constructor(message = "", ...args) {
        super(message, ...args);
        this.message = message;
        this.stack = "";
    }
}

function run(cmd) {
    try {
        return execSync(cmd);
    } catch (err) {
        return err.stderr.toString();
    }
}

function run_pwsh(cmd) {
    try {
        return execSync(cmd, { shell: "powershell" });
    } catch (err) {
        return err.stderr.toString();
    }
}
