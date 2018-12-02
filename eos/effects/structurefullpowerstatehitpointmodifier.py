# structureFullPowerStateHitpointModifier
#
# Used by:
# Items from category: Structure (17 of 17)
type = "passive"


def handler(fit, src, context):
    fit.ship.multiplyItemAttr("shieldCapacity", src.getModifiedItemAttr("structureFullPowerStateHitpointMultiplier") or 0)
    fit.ship.multiplyItemAttr("armorHP", src.getModifiedItemAttr("structureFullPowerStateHitpointMultiplier") or 0)
