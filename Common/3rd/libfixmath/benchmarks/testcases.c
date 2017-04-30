
/* Automatically generated testcases for fix16 operations
 * See generate_testcases.py for the generator.
 */

#include <fix16.h>

typedef struct {
    // Input
    fix16_t a;
    
    // Correct output
    fix16_t sqrt;
    fix16_t exp;
} fix16_1op_testcase;

typedef struct {
    // Inputs
    fix16_t a;
    fix16_t b;
    
    // Correct output
    fix16_t add;
    fix16_t sub;
    fix16_t mul;
    fix16_t div;
} fix16_2op_testcase;

#define TESTCASES1_COUNT (sizeof(testcases1)/sizeof(testcases1[0]))
#define TESTCASES2_COUNT (sizeof(testcases2)/sizeof(testcases2[0]))

static const fix16_1op_testcase testcases1[] = {
    {0x00000003, 0x000001bb, 0x00010003}, // 0
    {0xffff8000, 0x00000000, 0x00009b46}, // 1
    {0x00000003, 0x000001bb, 0x00010003}, // 2
    {0xa586901f, 0x00000000, 0x00000000}, // 3
    {0xffffc000, 0x00000000, 0x0000c75f}, // 4
    {0xfffe8c47, 0x00000000, 0x00003bed}, // 5
    {0x343a9126, 0x0073a194, 0x7fffffff}, // 6
    {0xfffc0000, 0x00000000, 0x000004b0}, // 7
    {0xfffffffb, 0x00000000, 0x0000fffb}, // 8
    {0x506c8396, 0x008f7cab, 0x7fffffff}, // 9
};

static const fix16_2op_testcase testcases2[] = {
    {0x000000b3, 0x00010000, 0x000100b3, 0xffff00b3, 0x000000b3, 0x000000b3}, // 0
    {0x506c8396, 0x00000025, 0x506c83bb, 0x506c8371, 0x000b9faf, 0x80000000}, // 1
    {0x00000004, 0xfffa0000, 0xfffa0004, 0x00060004, 0xffffffe8, 0xffffffff}, // 2
    {0xffffffaf, 0x07bc68b1, 0x07bc6860, 0xf84396fe, 0xfffd8d63, 0x00000000}, // 3
    {0x00005c01, 0x07bc68b1, 0x07bcc4b2, 0xf843f350, 0x02c7bd5c, 0x0000000c}, // 4
    {0x343a9126, 0x00005c01, 0x343aed27, 0x343a3525, 0x12c54064, 0x80000000}, // 5
    {0xfffe0001, 0x00000079, 0xfffe007a, 0xfffdff88, 0xffffff0e, 0xfbc4c4c3}, // 6
    {0x00000003, 0x0003ffff, 0x00040002, 0xfffc0004, 0x0000000c, 0x00000001}, // 7
    {0xffffffe6, 0xffffff5e, 0xffffff44, 0x00000088, 0x00000000, 0x00002916}, // 8
    {0x00000006, 0xffffffb1, 0xffffffb7, 0x00000055, 0x00000000, 0xffffec8f}, // 9
    {0x00050000, 0x00000008, 0x00050008, 0x0004fff8, 0x00000028, 0x80000000}, // 10
    {0x00000002, 0x00060000, 0x00060002, 0xfffa0002, 0x0000000c, 0x00000000}, // 11
    {0x00050000, 0xfffe8c47, 0x00038c47, 0x000673b9, 0xfff8bd63, 0xfffc8e7c}, // 12
    {0x506c8396, 0xffffff76, 0x506c830c, 0x506c8420, 0xffd4a581, 0x80000000}, // 13
    {0xfffff6d2, 0xffff0001, 0xfffef6d3, 0x0000f6d1, 0x0000092e, 0x0000092e}, // 14
    {0xffff0000, 0x00000008, 0xffff0008, 0xfffefff8, 0xfffffff8, 0xe0000000}, // 15
    {0x00002cc9, 0x00002000, 0x00004cc9, 0x00000cc9, 0x00000599, 0x00016648}, // 16
    {0x00030000, 0x0000ffff, 0x0003ffff, 0x00020001, 0x0002fffd, 0x00030003}, // 17
    {0x506c8396, 0xffffff76, 0x506c830c, 0x506c8420, 0xffd4a581, 0x80000000}, // 18
    {0x00000009, 0x00002cc9, 0x00002cd2, 0xffffd340, 0x00000002, 0x00000033}, // 19
    {0x00000005, 0x00050000, 0x00050005, 0xfffb0005, 0x00000019, 0x00000001}, // 20
    {0x0000ff73, 0xffffff5e, 0x0000fed1, 0x00010015, 0xffffff5e, 0xfe6c53c1}, // 21
    {0x947943d4, 0x000068fa, 0x9479acce, 0x9478dada, 0xd3e841fa, 0x80000000}, // 22
    {0xffffe000, 0x00010000, 0x0000e000, 0xfffee000, 0xffffe000, 0xffffe000}, // 23
    {0xfffffffd, 0x8e086b99, 0x8e086b96, 0x71f79464, 0x000155e7, 0x00000000}, // 24
    {0x00002000, 0xfffff6d2, 0x000016d2, 0x0000292e, 0xfffffeda, 0xfffc8398}, // 25
    {0x00020000, 0xfffc0000, 0xfffe0000, 0x00060000, 0xfff80000, 0xffff8000}, // 26
    {0xffff0000, 0x0000bf85, 0xffffbf85, 0xfffe407b, 0xffff407b, 0xfffea9cf}, // 27
    {0xffffffaf, 0x000068fa, 0x000068a9, 0xffff96b5, 0xffffffdf, 0xffffff3a}, // 28
    {0xffffff5e, 0x00000025, 0xffffff83, 0xffffff39, 0x00000000, 0xfffb9f23}, // 29
    {0xffff0000, 0xfffffff7, 0xfffefff7, 0xffff0009, 0x00000009, 0x1c71c71c}, // 30
    {0xfffd0000, 0x0001ffff, 0xfffeffff, 0xfffb0001, 0xfffa0003, 0xfffe7fff}, // 31
    {0x00000004, 0x00005c01, 0x00005c05, 0xffffa403, 0x00000001, 0x0000000b}, // 32
    {0x00040000, 0x00000005, 0x00040005, 0x0003fffb, 0x00000014, 0x80000000}, // 33
    {0x1a9ca0ec, 0x00000001, 0x1a9ca0ed, 0x1a9ca0eb, 0x00001a9d, 0x80000000}, // 34
    {0xfffffffb, 0x00000002, 0xfffffffd, 0xfffffff9, 0x00000000, 0xfffd8000}, // 35
    {0x000000af, 0x00060000, 0x000600af, 0xfffa00af, 0x0000041a, 0x0000001d}, // 36
    {0xfffffffe, 0x000068fa, 0x000068f8, 0xffff9704, 0xffffffff, 0xfffffffb}, // 37
    {0x00004000, 0x000000b3, 0x000040b3, 0x00003f4d, 0x0000002d, 0x005b87de}, // 38
    {0x07bc68b1, 0xffffdf3f, 0x07bc47f0, 0x07bc8972, 0xff029ddf, 0xc38965ca}, // 39
    {0xfffb0000, 0x0000000a, 0xfffb000a, 0xfffafff6, 0xffffffce, 0x80000000}, // 40
    {0x947943d4, 0xffffff5e, 0x94794332, 0x94794476, 0x00440b43, 0x80000000}, // 41
    {0x33992913, 0xfffffff6, 0x33992909, 0x3399291d, 0xfffdfc04, 0x80000000}, // 42
    {0x00002cc9, 0x00004000, 0x00006cc9, 0xffffecc9, 0x00000b32, 0x0000b324}, // 43
    {0x00000002, 0xfffc0000, 0xfffc0002, 0x00040002, 0xfffffff8, 0xffffffff}, // 44
    {0x000068fa, 0xfffe8c47, 0xfffef541, 0x0001dcb3, 0xffff6792, 0xffffb7b4}, // 45
    {0x8e086b99, 0x000000af, 0x8e086c48, 0x8e086aea, 0xffb217c2, 0x80000000}, // 46
    {0x0000ffff, 0x00008000, 0x00017fff, 0x00007fff, 0x00008000, 0x0001fffe}, // 47
    {0x00000001, 0x07bc68b1, 0x07bc68b2, 0xf8439750, 0x000007bc, 0x00000000}, // 48
    {0xffffdf3f, 0x00005c01, 0x00003b40, 0xffff833e, 0xfffff43b, 0xffffa4dd}, // 49
};
