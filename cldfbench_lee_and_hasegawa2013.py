import pathlib

import nexus
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee_and_hasegawa2013"

    def cmd_makecldf(self, args):
        self.init(args)
        # args.writer.add_summary(
        #     self.raw_dir.read_tree('Ainu_SDollo_GRW.mcct.trees', detranslate=True),
        #     self.metadata,
        #     args.log)
        #
        # set burn-in to 1001, take the rest
        posterior = self.raw_dir.read_trees(
            'Ainu_SDollo_GRW.trees.gz',
            burnin=1001, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('Ainu.nex'),
            self.characters,
            args.log)
            


            