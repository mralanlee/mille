package main

import (
	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "mille",
	Short: "Terraform/OpenTofu plan visualization tool",
	Run: func(cmd *cobra.Command, args []string) {
		log.Info("Mille CLI - coming soon!")
	},
}

func main() {
	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}
