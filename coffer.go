package main

import (
	"fmt"
	"os"

	"github.com/jessevdk/go-flags"
)

const execName = "coffer"

type options struct {
	Verbose []bool `short:"v" long:"verbose" description:"Show detailed output"`
	Version bool   `long:"version" description:"Show version number"`
}

var cliOptions = options{}

var parser = flags.NewParser(&cliOptions, flags.HelpFlag|flags.PassDoubleDash)

func init() {
	parser.AddCommand("master", "master short", "master long", &masterCommand{})
}

type masterCommand struct {
	Something string `short:"s" long:"something" description:"dummy"`
}

func main() {
	_, err := parser.Parse()
	if cliOptions.Version {
		fmt.Println(execName + "dev build")
	}
	if err != nil {
		if e, ok := err.(*flags.Error); ok {
			if e.Type == flags.ErrHelp {
				fmt.Println(err)
				return
			}
		}
		fmt.Println(err)
		os.Exit(1)
	}
}
