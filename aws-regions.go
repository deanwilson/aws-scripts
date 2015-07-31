package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
	"text/tabwriter"
)

func main() {

	regions := map[string]string{
		"ap-northeast-1": "Asia Pacific (Tokyo)",
		"ap-southeast-1": "Asia Pacific (Singapore)",
		"ap-southeast-2": "Asia Pacific (Sydney)",
		"eu-central-1":   "EU (Frankfurt)",
		"eu-west-1":      "EU (Ireland)",
		"sa-east-1":      "South America (Sao Paulo)",
		"us-east-1":      "US East (N. Virginia)",
		"us-west-1":      "US West (N. California)",
		"us-west-2":      "US West (Oregon)",
	}

	// short cut if given an exact region
	region := ""
	if len(os.Args) > 1 {
		region = os.Args[1]

		if desc, ok := regions[region]; ok {
			fmt.Println(desc)
			os.Exit(0)
		}
	}

	w := new(tabwriter.Writer)
	w.Init(os.Stdout, 30, 0, 2, ' ', 0)

	var keys []string
	for k := range regions {
		keys = append(keys, k)
	}

	sort.Strings(keys)

	for _, k := range keys {
		if strings.Contains(k, region) {
			fmt.Fprintln(w, k, "\t", regions[k])
		}
	}
	w.Flush()
}
