"""
MCNP translation cards TR
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle


class Transformation:
    def __init__(self):
        self.alpha = 0
        self.beta = 0
        self.gamma = 0
        self.trans = [0, 0, 0]
        self.x, self.y, self.z = 0, 0, 0
        self.xt, self.yt, self.zt = 0, 0, 0
        self.x0, self.y0, self.z0 = 0, 0, 0
        self.h_points = 20
        self.base_points = 50
        self.height = 0
        self.radius = 0
        self.axis = 0
        self.mcnp = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def make_cylinder(self, x0, y0, z0, height, radius, axis="z"):
        # divide the circle into base_points equal parts
        u = np.linspace(0, 2 * np.pi, self.base_points)
        # divide the height into h_points
        h = np.linspace(0, height, self.h_points)
        if axis == "z":
            # x value repeated h_points times
            x = radius * np.outer(np.sin(u), np.ones(len(h))) + x0
            # y value repeated h_points times
            y = radius * np.outer(np.cos(u), np.ones(len(h))) + y0
            # x,y corresponding height
            z = np.outer(np.ones(len(u)), h) + z0
        elif axis == "x":
            x = np.outer(np.ones(len(u)), h) + x0
            y = radius * np.outer(np.sin(u), np.ones(len(h))) + y0
            z = radius * np.outer(np.cos(u), np.ones(len(h))) + z0
        elif axis == "y":
            x = radius * np.outer(np.sin(u), np.ones(len(h))) + x0
            y = np.outer(np.ones(len(u)), h) + y0
            z = radius * np.outer(np.cos(u), np.ones(len(h))) + z0
        self.height = height
        self.radius = radius
        self.axis = axis
        self.x = x
        self.y = y
        self.z = z
        self.xt = x
        self.yt = y
        self.zt = z
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

    @staticmethod
    def rot_x(alpha, sense="CCW"):
        ## rotation matrices
        """a00 a01 a02

        a10 a11 a12

        a20 a21 a22"""
        if sense == "CCW":
            m = 1
        elif sense == "CW":
            m = -1

        a00 = 1
        a01 = 0
        a02 = 0
        a10 = 0
        a11 = np.cos(np.deg2rad(alpha))
        a12 = -m * np.sin(np.deg2rad(alpha))
        a20 = 0
        a21 = m * np.sin(np.deg2rad(alpha))
        a22 = np.cos(np.deg2rad(alpha))

        Tx = np.array([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])
        return Tx

    @staticmethod
    def rot_y(beta, sense="CCW"):
        if sense == "CCW":
            m = 1
        elif sense == "CW":
            m = -1

        a00 = np.cos(np.deg2rad(beta))
        a01 = 0
        a02 = m * np.sin(np.deg2rad(beta))
        a10 = 0
        a11 = 1
        a12 = 0
        a20 = -m * np.sin(np.deg2rad(beta))
        a21 = 0
        a22 = np.cos(np.deg2rad(beta))

        Ty = np.array([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])
        return Ty

    @staticmethod
    def rot_z(gamma, sense="CCW"):
        if sense == "CCW":
            m = 1
        elif sense == "CW":
            m = -1

        a00 = np.cos(np.deg2rad(gamma))
        a01 = -m * np.sin(np.deg2rad(gamma))
        a02 = 0
        a10 = m * np.sin(np.deg2rad(gamma))
        a11 = np.cos(np.deg2rad(gamma))
        a12 = 0
        a20 = 0
        a21 = 0
        a22 = 1

        Tz = np.array([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])
        return Tz

    def make_transformation(self, alpha, beta, gamma, trans=[0, 0, 0]):
        Tx = self.rot_x(alpha, "CCW")
        Ty = self.rot_y(beta, "CCW")
        Tz = self.rot_z(gamma, "CCW")

        x0, y0, z0 = trans[0], trans[1], trans[2]

        xp = self.x.reshape((self.base_points * self.h_points, 1), order="F")
        yp = self.y.reshape((self.base_points * self.h_points, 1), order="F")
        zp = self.z.reshape((self.base_points * self.h_points, 1), order="F")

        # order: x, y, z
        M_trans = np.array([x0, y0, z0])
        xyz = np.hstack((xp, yp, zp))

        xyz_x = np.dot(Tx, xyz.T).T
        xyz_y = np.dot(Ty, xyz_x.T).T
        xyz_z = np.dot(Tz, xyz_y.T).T

        xyz2 = xyz_z
        # xyz2 = (M_rot@xyz.T).T

        x2, y2, z2 = (
            xyz2[:, 0] + M_trans[0],
            xyz2[:, 1] + M_trans[1],
            xyz2[:, 2] + M_trans[2],
        )

        x2d = x2.reshape((self.base_points, self.h_points), order="F")
        y2d = y2.reshape((self.base_points, self.h_points), order="F")
        z2d = z2.reshape((self.base_points, self.h_points), order="F")

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.mcnp_matrix()
        self.trans = trans
        self.xt = x2d
        self.yt = y2d
        self.zt = z2d

    def mcnp_matrix(self):
        Tx2 = self.rot_x(self.alpha, "CW")
        Ty2 = self.rot_y(self.beta, "CW")
        Tz2 = self.rot_z(self.gamma, "CW")
        # order: x, y, z
        self.mcnp = np.round(Tx2 @ Ty2 @ Tz2, decimals=2)

    # Plot the surface
    def plot_surf(self, ax_3d, color="black", soil=False, plot_axes=False):
        if soil:  #  add end caps to the cylinder
            ax_3d.plot_surface(self.xt, self.yt, self.zt, color="blue", alpha=1)
            # end_cap1 = Circle((self.x0, self.y0),
            #                   radius=self.radius, color="blue")
            # ax_3d.add_patch(end_cap1)
            # art3d.pathpatch_2d_to_3d(end_cap1, z=self.z0, zdir=self.axis)

            # end_cap2 = Circle((self.x0, self.y0),
            #             radius=self.radius, color="blue")
            # ax_3d.add_patch(end_cap2)
            # art3d.pathpatch_2d_to_3d(end_cap2, z=self.z0+self.height,
            #                           zdir=self.axis)
        else:
            ax_3d.plot_surface(self.xt, self.yt, self.zt, color=color, alpha=1)

        ax_3d.set_xlabel("X")
        ax_3d.set_ylabel("Y")
        ax_3d.set_zlabel("Z")

        ax_3d.spines["bottom"].set_color("red")
        ax_3d.spines["top"].set_color("red")
        ax_3d.xaxis.label.set_color("red")
        ax_3d.tick_params(axis="x", colors="red")
        ax_3d.yaxis.label.set_color("green")
        ax_3d.tick_params(axis="y", colors="green")
        ax_3d.zaxis.label.set_color("blue")
        ax_3d.tick_params(axis="z", colors="blue")

        if plot_axes:
            self.plot_axes(ax_3d)
            self.axisEqual3D(ax_3d)

    def plot_axes(self, ax_3d, ax_length=None):
        if ax_length is None:
            ax_length = max(abs(self.x.max()), abs(self.y.max()), abs(self.z.max()))

        ax_3d.quiver(
            0,
            0,
            0,
            ax_length + 5,
            0,
            0,
            color="red",
            alpha=0.5,
            arrow_length_ratio=0.05,
        )
        ax_3d.quiver(
            0,
            0,
            0,
            0,
            ax_length + 5,
            0,
            color="green",
            alpha=0.5,
            arrow_length_ratio=0.05,
        )
        ax_3d.quiver(
            0,
            0,
            0,
            0,
            0,
            ax_length + 5,
            color="blue",
            alpha=0.5,
            arrow_length_ratio=0.05,
        )

    @staticmethod
    def axisEqual3D(ax):
        extents = np.array([getattr(ax, f"get_{dim}lim")() for dim in "xyz"])
        sz = extents[:, 1] - extents[:, 0]
        centers = np.mean(extents, axis=1)
        maxsize = max(abs(sz))
        r = maxsize / 2
        for ctr, dim in zip(centers, "xyz"):
            getattr(ax, f"set_{dim}lim")(ctr - r, ctr + r)
