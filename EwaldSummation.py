import numpy as np

class EwaldSummation:

    VACUUM_PERMITTIVITY = 1

    @staticmethod
    def calculate_overall_energy(system, parameters):
        raise NotImplementedError

    @staticmethod
    def _calculate_longranged_energy(system, parameters):
        raise NotImplementedError

    @staticmethod
    def _calculate_shortranged_energy(system, parameters):
        raise NotImplementedError

    @staticmethod
    def _calculate_selfinteraction_energy(system, parameters):
        selfinteraction_energy = 0
        prefactor = 1 / (2 * EwaldSummation.VACUUM_PERMITTIVITY * parameters.es_sigma * (2 * np.pi) ** (3/2))

        for i in range(0, len(system.particles)):
            selfinteraction_energy += system.particles[i].charge ** 2

        return prefactor * selfinteraction_energy