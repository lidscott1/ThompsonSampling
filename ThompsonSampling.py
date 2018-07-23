from numpy.random import beta

sites = ["var_1", "var_2", "var_3"]


class ThompsonSampling(object):

    def __init__(self, variation_list):

        self.variations = variation_list

        self.distributions = {}

        for variation in self.variations:

            self.distributions[variation] = {"alpha": 1, "beta":1}

        self.variation_selected = False

    def select_variation(self):

        highest_prob = -1

        selected = None

        for variation in self.variations:

            alpha_i, beta_i = self.distributions[variation]["alpha"], self.distributions[variation]["beta"]

            candidate_prob = beta(alpha_i, beta_i)

            if candidate_prob > highest_prob:

                highest_prob = candidate_prob

                selected = variation

        print(selected)

        self.selected = selected

        self.variation_selected = True

    def update_params(self, positive_response):

        assert self.variation_selected, "You have not selected a new variation"

        if positive_response:

            self.distributions[self.selected]["alpha"] += 1

        else:

            self.distributions[self.selected]["beta"] += 1

        self.variation_selected = False

ts_variations = ThompsonSampling(sites)

ts_variations.select_variation()

ts_variations.update_params(True)

ts_variations.update_params(True)

ts_variations.select_variation()

ts_variations.update_params(False)
