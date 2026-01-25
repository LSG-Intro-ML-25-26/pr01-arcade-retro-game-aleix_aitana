// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level":
            case "level1":return tiles.createTilemap(hex`2600140001080d080808080d080808080d08031213131313131313131313131313131313131313131315060a0a0a0a0a0a0a0a0a0a0a0a0a0701080d08080d080301080d080d080d080301080d0803170f0a0a0a0a0a0a0a0a0a0a0a0a0a07060a0a0a0a0a0a07061c0a0a0a0a0a1c07060a0a0a1a17060a0a0a0a0a0a0a0a0a0a0a0a0a070f0a1b1b1b1b0a07060a0a0a0a0a0a0a10110a1b0a0717060a0a0a0a161616160a0a0a0a0a07060a1b0a0a1b0a070f0a0a0a0a0a0a0a10110a1b0a0717060a0a0a0a161215160a0a0a0a0a07060a1b0a0a1b0a10110a0a0a0a0a0a0a1a0f0a1b0a1a170f0a0a0a0a161814160a0a0a0a0a07090a1b0a0a1b0a10110a0a0a0a0a0a0a07090a0a0a0717060a0a0a0a161616160a0a0a0a0a070f0a1b0a0a1b0a07060a0a0a0a0a0a0a07090a1b0a0717060a0a0a0a0a0a0a0a0a0a0a0a0a07060a1b1b1b1b0a070f0a0a0a0a0a0a0a1a0f0a1b0a07170f0a0a0a0a0a0a0a0a0a0a0a0a0a07060a0a0a0a0a0a07061c0a0a0a0a0a1b07090a1b0a1a17090a0a0a0a0a0a0a0a0a0a0a0a0a070205050b0b050504020505050505050504090a1b0a0717020505050b0b05050505050505050401080d0c0c08080301080d080d080d08030f0a0a0a07170108080d0c0c080808080d080808030f0a0a0a0a0a0a07060a0a0a0a0a0a0a07090a1b0a0717090a0a0a0a0a0a0a0a0a0a0a0a0a07090a0a0a0a0a0a070f0a0a0a0a0a0a0a1a090a1b0a1a170f0a0a0a0a0a0a0a0a0a0a0a0a0a07090a0a0a0a0a0a10110a0a0a0a0a0a0a070f0a1b0a0717090a1b1b1b1b0a0a1b1b1b1b0a0a10110a0a0a0a0a0a10110a0a0a0a0a0a0a07090a1b0a0717090a1b1b1b1b0a0a1b1b1b1b0a0a10110a0a0a0a0a0a07060a0a0a0a0a0a0a1a090a1b0a07170f0a1b1b1b1b0a0a1b1b1b1b0a0a070f0a0a0a0a0a0a070f0a0a0a0a0a0a0a070f0a0a0a1a17090a0a0a0a0a0a0a0a0a0a0a0a0a07090a0a0a0a0a0a07060a0a0a0a0a0a0a0702050e05041702050e050505050e050505050e050402050e05050e050402050e0505050e0504181919191914`, img`
22222222222222222222222222222222222222
2.............222222222222222222222222
2.............22......22.......22...22
2.............22......22............22
2.............22......22............22
2.....22......22...............22...22
2.....22......22...............22...22
2.............22......22.......22...22
2.............22......22.......22...22
2.............22......22.......22...22
2.............2222..2222222222222...22
2222..222222222222..2222222222222...22
2222..2222222222......22.......22...22
2.............22......22.......22...22
2.............22...............22...22
2..............................22...22
2.....................22.......22...22
2.............22......22.......22...22
2.............22......22.......2222222
22222222222222222222222222222222222222
`, [myTiles.transparency16,sprites.dungeon.purpleOuterNorthWest,sprites.dungeon.purpleOuterSouthEast,sprites.dungeon.purpleOuterNorthEast,sprites.dungeon.purpleOuterSouthWest,sprites.dungeon.purpleOuterSouth1,sprites.dungeon.purpleOuterWest0,sprites.dungeon.purpleOuterEast0,sprites.dungeon.purpleOuterNorth1,sprites.dungeon.purpleOuterWest1,sprites.dungeon.floorDark2,sprites.dungeon.stairSouth,sprites.dungeon.stairNorth,sprites.dungeon.purpleOuterNorth2,sprites.dungeon.purpleOuterSouth2,sprites.dungeon.purpleOuterWest2,sprites.dungeon.stairEast,sprites.dungeon.stairWest,sprites.dungeon.darkGroundNorthWest0,sprites.dungeon.darkGroundNorth,sprites.dungeon.darkGroundSouthEast0,sprites.dungeon.darkGroundNorthEast0,sprites.dungeon.floorDarkDiamond,sprites.dungeon.darkGroundEast,sprites.dungeon.darkGroundSouthWest0,sprites.dungeon.darkGroundSouth,sprites.dungeon.purpleOuterEast2,sprites.dungeon.floorDark0,sprites.dungeon.floorDark4], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "tile1":return tile1;
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
