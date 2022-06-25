import pathlib

import nexus
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee_and_hasegawa2013"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree('Ainu_SDollo_GRW.mcct.trees', detranslate=True),
            self.metadata,
            args.log)
        
        # set burn-in to 1001, take the rest
        posterior = self.read_nexus(self.raw_dir / 'Ainu_SDollo_GRW.trees.gz')
        posterior = self.remove_burnin(posterior, 1001)
        posterior.trees.detranslate()
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('Ainu.nex'),
            self.characters,
            args.log)