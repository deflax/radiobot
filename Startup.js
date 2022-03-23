var toml = require("toml");
var fs = require("fs");
var Radio = require("./Radio");

class Startup
{
	constructor()
	{
		this.radios = [];

		let configFile = process.env.CONFIG_FILE || "config.toml";
		this.config = toml.parse(fs.readFileSync(configFile, "utf8"));
	}

	run()
	{
		this.setupRadio();
	}

	setupRadio()
	{
		if (this.config.radios === undefined) {
			console.error('No radios are defined in the config file, exiting...');
			process.exit(1);
		}
		for (let i = 0; i < this.config.radios.length; i++) {
			this.startRadio(this.config.radios[i]);
		}
		this.setupSignals();
	}

	startRadio(radioConfig)
	{
		this.radios.push(new Radio(this.config, radioConfig));
	}

	setupSignals()
	{
		var stopHandler = () => {
			if (this.bot) {
				this.bot.stop();
			}
			for (var i = 0; i < this.radios.length; i++) {
				this.radios[i].stop();
			}
		};
		process.on("SIGINT", stopHandler); // Ctrl+C
		process.on("SIGTERM", stopHandler); // Terminate
	}
}

module.exports = Startup;
