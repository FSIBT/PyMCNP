import pymcnp
from .... import classes


class Test_Event(classes.Test_FromMcnp, classes.Test_ToDataframe):
    element = pymcnp.ptrac.block.Event

    EXAMPLES_FROM_MCNP_VALID = [
        '       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01',
        '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01',
    ]

    def test_particle(self) -> None:
        """
        Tests `particle` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.particle

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.particle

    def test_material(self) -> None:
        """
        Tests `material` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.material

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.material

    def test_position(self) -> None:
        """
        Tests `position` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.position

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.position

    def test_zaid(self) -> None:
        """
        Tests `zaid` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.zaid

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.zaid

    def test_surface(self) -> None:
        """
        Tests `surface` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.surface

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.surface

    def test_direction(self) -> None:
        """
        Tests `direction` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.direction

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.direction

    def test_energy(self) -> None:
        """
        Tests `energy` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.energy

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.energy

    def test_weight(self) -> None:
        """
        Tests `weight` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.weight

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.weight

    def test_time(self) -> None:
        """
        Tests `time` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            event, _ = pymcnp.ptrac.block.Event.from_mcnp('       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01')
            _ = event.time

        event, _ = pymcnp.ptrac.block.EventSource_3.from_mcnp(
            '       3000         1        40         1         4         4\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventSource_4.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventBank_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventBank_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventSurface_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventSurface_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventCollision_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventCollision_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventTermination_3.from_mcnp(
            '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
        event, _ = pymcnp.ptrac.block.EventTermination_4.from_mcnp(
            '       3000         1        40         1         4         4         0         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00'
        )
        _ = event.time
