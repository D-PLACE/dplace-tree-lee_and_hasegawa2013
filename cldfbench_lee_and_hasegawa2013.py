import re
import pathlib

import nexus
import phlorest

RATE_PATTERN = re.compile(r':\[&rate=[0-9]*\.?[0-9]*]')


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee_and_hasegawa2013"

    def cmd_makecldf(self, args):
        """
summary.trees: original/Ainu_SDollo_GRW.mcct.trees
	cp $< $@

posterior.trees: original/Ainu_SDollo_GRW.trees.gz
	nexus trees -c -n 1000 $< -o $@

data.nex:
	cp original/Ainu.nex $@
        """
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                nexus.NexusReader.from_string(
                    RATE_PATTERN.sub(':', self.raw_dir.read('Ainu_SDollo_GRW.mcct.trees'))),
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.read_gzipped_text(self.raw_dir / 'Ainu_SDollo_GRW.trees.gz'),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'Ainu.nex')
