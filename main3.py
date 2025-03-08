import cmath
import math


class VoltagePhasor:
    """Represents a voltage phasor in polar form (magnitude and phase angle)"""

    def __init__(self, magnitude=0, angle_degrees=0):
        if magnitude < 0:
            raise ValueError("Voltage magnitude cannot be negative")
        self.magnitude = magnitude  # in volts
        self.angle_degrees = angle_degrees  # in degrees

    def to_complex(self):
        """Convert to rectangular form (complex number)"""
        return cmath.rect(self.magnitude, math.radians(self.angle_degrees))

    def __add__(self, other):
        """Add two voltage phasors using vector addition"""
        if not isinstance(other, VoltagePhasor):
            raise TypeError("Can only add VoltagePhasor to other VoltagePhasor")

        total = self.to_complex() + other.to_complex()
        mag, ang_rad = cmath.polar(total)
        return VoltagePhasor(mag, math.degrees(ang_rad))

    def __repr__(self):
        return f"VoltagePhasor({self.magnitude:.2f} V ∠ {self.angle_degrees:.2f}°)"


class CurrentPhasor:
    """Represents a current phasor in polar form (magnitude and phase angle)"""

    def __init__(self, magnitude=0, angle_degrees=0):
        if magnitude < 0:
            raise ValueError("Current magnitude cannot be negative")
        self.magnitude = magnitude  # in amps
        self.angle_degrees = angle_degrees  # in degrees

    def to_complex(self):
        """Convert to rectangular form (complex number)"""
        return cmath.rect(self.magnitude, math.radians(self.angle_degrees))

    def __add__(self, other):
        """Add two current phasors using vector addition"""
        if not isinstance(other, CurrentPhasor):
            raise TypeError("Can only add CurrentPhasor to other CurrentPhasor")

        total = self.to_complex() + other.to_complex()
        mag, ang_rad = cmath.polar(total)
        return CurrentPhasor(mag, math.degrees(ang_rad))

    def __repr__(self):
        return f"CurrentPhasor({self.magnitude:.2f} A ∠ {self.angle_degrees:.2f}°)"


class Power:
    """Represents electrical power in complex form"""

    def __init__(self, complex_power):
        """
        Args:
            complex_power (complex): Complex power (S = P + jQ) in VA
        """
        self.complex_power = complex_power

    @property
    def real_power(self):
        """Active power in watts (P)"""
        return self.complex_power.real

    @property
    def reactive_power(self):
        """Reactive power in VAR (Q)"""
        return self.complex_power.imag

    @property
    def apparent_power(self):
        """Apparent power in VA (|S|)"""
        return abs(self.complex_power)

    @property
    def power_factor(self):
        """Power factor (PF)"""
        return math.cos(math.atan2(self.reactive_power, self.real_power))

    def __mul__(self, other):
        """Multiply power by a scalar"""
        if isinstance(other, (int, float)):
            return Power(self.complex_power * other)
        raise TypeError("Power can only be multiplied by scalars")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return (f"Power: {self.real_power:.2f} W + "
                f"{self.reactive_power:.2f} VAR j (PF={self.power_factor:.2f})")


# Define phasor multiplication operator
def voltage_current_multiplier(v, i):
    """Multiply voltage phasor by current phasor to get complex power"""
    if isinstance(v, VoltagePhasor) and isinstance(i, CurrentPhasor):
        # S = V × I* (complex conjugate of current)
        return Power(v.to_complex() * i.to_complex().conjugate())
    raise TypeError("Multiplication requires VoltagePhasor and CurrentPhasor")


# Overload multiplication operator
VoltagePhasor.__mul__ = voltage_current_multiplier
CurrentPhasor.__rmul__ = voltage_current_multiplier

