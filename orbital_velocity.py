
import math

def calculate_orbital_velocity(mass_of_central_body, orbital_radius):
    """
    Calculates the orbital velocity of a satellite.

    Args:
        mass_of_central_body (float): The mass of the central body in kilograms (e.g., Earth, Sun).
        orbital_radius (float): The distance from the center of the central body to the satellite in meters.

    Returns:
        float: The orbital velocity in meters per second.
    """
    G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
    velocity = math.sqrt((G * mass_of_central_body) / orbital_radius)
    return velocity

if __name__ == "__main__":
    # Example for Earth's orbit (approximate values for LEO)
    earth_mass = 5.972e24  # kg
    earth_radius = 6.371e6  # meters
    altitude = 400e3  # 400 km in meters (Low Earth Orbit)
    orbital_radius_leo = earth_radius + altitude

    leo_velocity = calculate_orbital_velocity(earth_mass, orbital_radius_leo)
    print(f"Orbital velocity for LEO (altitude 400km): {leo_velocity:.2f} m/s")

    # Example for geostationary orbit
    geostationary_altitude = 35786e3 # meters
    orbital_radius_geo = earth_radius + geostationary_altitude
    geo_velocity = calculate_orbital_velocity(earth_mass, orbital_radius_geo)
    print(f"Orbital velocity for Geostationary Orbit: {geo_velocity:.2f} m/s")
