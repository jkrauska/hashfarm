# hashfarm
Random adjective color animals for making things more memorable

In my $dayjob I need to look up unique hash strings on occasion, and I was getting tired of carrying around long strings like '3750318906711016457541286099781521507492567885'.  So I wondered how hard it would be to make a simple and short mapping of a random string input to a friendly short phrase.

This is somewhat stolen from [XKCD's 'correct horse staple' musings](https://xkcd.com/936/), but implemented as a public one way hash to a friendly shared name.  It also takes some influence and adjectives from [Docker's naming scheme for containers](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go).

I like animals a lot, so I started with just mixing colors and animals.  But that wasn't amusing enough, so I added some adjectives to add some excitement and emotion to the mix.

The current list is ~100 adjectives, ~100 colors and ~100 animals, yielding ~1M unique 3 word phrases.  This felt reasonably wide to avoid too many collisions for trivial use cases.

I'm using python's fileinput so you can echo directly to the program via stdin, or have it read a file and give you a hash per line of the file.

Like so:
```bash
$ cat /dev/random | ./hashme.py | head -10
tender_tangerine_crab
naughty_tan_elephant
hopeful_chartreuse_gnat
tender_peach_seal
ecstatic_copper_crab
gallant_cornflower_cockroach
adoring_silver_monkey
sweet_champagne_buffalo
keen_platinum_tiger
angry_chestnut_goat
```

I am a lot happier searching for an 'adoring_silver_monkey' than '3750318906711016457541286099781521507492567885' anyday.
