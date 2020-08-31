import numpy
import fvm
import pytest

def create_coordinate_vector(dx):
    return numpy.roll(numpy.arange(-dx, 1+dx, dx), -2)

def test_u_xx():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.u_xx(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 0, 1, 1] == pytest.approx(1 / dx * dy * dz)
                assert atom[i, j, k, 2, 1, 1] == pytest.approx(1 / dx * dy * dz)

def test_v_yy():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.v_yy(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 1, 0, 1] == pytest.approx(1 / dy * dx * dz)
                assert atom[i, j, k, 1, 2, 1] == pytest.approx(1 / dy * dx * dz)

def test_w_zz():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.w_zz(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 1, 1, 0] == pytest.approx(1 / dz * dy * dx)
                assert atom[i, j, k, 1, 1, 2] == pytest.approx(1 / dz * dy * dx)

def test_u_yy():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.u_yy(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 0, 1, 1] == pytest.approx(1 / dy * dx * dz)
                assert atom[i, j, k, 2, 1, 1] == pytest.approx(1 / dy * dx * dz)

def test_v_xx():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.v_xx(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 1, 0, 1] == pytest.approx(1 / dx * dy * dz)
                assert atom[i, j, k, 1, 2, 1] == pytest.approx(1 / dx * dy * dz)

def test_w_yy():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.w_yy(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 1, 1, 0] == pytest.approx(1 / dy * dz * dx)
                assert atom[i, j, k, 1, 1, 2] == pytest.approx(1 / dy * dz * dx)

def test_u_zz():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.u_zz(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 0, 1, 1] == pytest.approx(1 / dz * dx * dy)
                assert atom[i, j, k, 2, 1, 1] == pytest.approx(1 / dz * dx * dy)

def test_v_zz():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.v_zz(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 1, 0, 1] == pytest.approx(1 / dz * dy * dx)
                assert atom[i, j, k, 1, 2, 1] == pytest.approx(1 / dz * dy * dx)

def test_w_xx():
    nx = 5
    ny = 3
    nz = 2

    dx = 1 / (nx + 1)
    dy = 1 / (ny + 1)
    dz = 1 / (nz + 1)

    x = create_coordinate_vector(dx)
    y = create_coordinate_vector(dy)
    z = create_coordinate_vector(dz)

    atom = numpy.zeros([nx, ny, nz, 3, 3, 3])
    fvm.Derivatives.w_xx(atom, nx, ny, nz, x, y, z)

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                print(i, j, k)
                assert atom[i, j, k, 1, 1, 0] == pytest.approx(1 / dx * dz * dy)
                assert atom[i, j, k, 1, 1, 2] == pytest.approx(1 / dx * dz * dy)
