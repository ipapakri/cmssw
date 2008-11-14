import FWCore.ParameterSet.Config as cms

from RecoTracker.TkTrackingRegions.GlobalTrackingRegionWithVertices_cfi import *
globalSeedsFromPairsWithVertices = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    #include "RecoTracker/PixelStubs/data/SeedComparitorWithPixelStubs.cfi"
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('MixedLayerPairs')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSetWithVerticesBlock,
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer')
    ),
    propagator = cms.string('PropagatorWithMaterial'),
# The fast-helix fit works well, except for large impact parameter pixel pair seeding.
    UseFastHelix = cms.bool(True),
# Following parameter not relevant for UseFastHelix = False.                                                                                     
    SeedMomentumForBOFF = cms.double(5.0), 
    TTRHBuilder = cms.string('WithTrackAngle')
)


