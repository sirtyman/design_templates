# References
- [The Repository](https://github.com/sirtyman/design_templates/new/master)
- [ATP](https://a_link_to_ATP.com)

# User Applications
- Application X
- Application Y
- Application Z

# Test Bed diagram

@startuml

skinparam componentStyle rectangle

package "Chassis1" {
  [DUT] - [Adapter1]: Backplane
}

package "Remote Chassis" {
[Adapter1] - [Adapter2]: Ethernet
[Adapter2] - [IO]: Backplane
}

@enduml

# Preconditions
- DUT is in the X state
- Application X downloaded to DUT
- Task A is inhibited
- All connections with external devices are set
- All connections are not flickering over 20 s

# Test Scenarios

## Scenario 1
- **Given** DUT connected to the Ethernet
And connection rate set to the highest rate
- **When** uninhibitting task
And when waiting TEST_WAIT time [s]
- **Then** All connections are preserved during the TEST_WAIT time
And data integrity is preserved during the TEST_WAIT time

# Postconditions
- Blanc the DUT
