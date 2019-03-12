'''
WARNING:
Around 4000 PNG images will be created threrefore change the file creation path accordingly.
'''

import string
import  PIL
from PIL import Image

# encrypted PNG Image
encrypted = [0xCA, 0x04, 0x0D, 0x11, 0x5A, 0x53, 0x52, 0x53, 0x50, 0x39, 0x46, 0x3F, 0x11, 0x7C, 0x1D, 0x6A,
0x4D, 0x51, 0x43, 0x1C, 0x36, 0x56, 0x4B, 0x70, 0x4C, 0x45, 0x54, 0x43, 0x56, 0x36, 0x99, 0x46,
0x36, 0x50, 0x39, 0x40, 0xC2, 0x11, 0x70, 0x18, 0x6C, 0x35, 0x0F, 0xAF, 0xCB, 0xFD, 0xC3, 0x90,
0x07, 0x48, 0x43, 0xCD, 0x21, 0x24, 0x9E, 0x12, 0x4D, 0x77, 0x71, 0xBC, 0xBE, 0xDE, 0x7A, 0x66,
0xD9, 0xF7, 0x63, 0x35, 0x09, 0x8E, 0x10, 0xE0, 0x53, 0xD2, 0x1D, 0x1D, 0xA9, 0x4A, 0xA6, 0x7C,
0x40, 0x42, 0x3E, 0xFF, 0x0F, 0x63, 0x40, 0x58, 0x7A, 0x19, 0x6A, 0x3F, 0x2F, 0x7A, 0xA8, 0x16,
0x56, 0x4A, 0x3F, 0x04, 0x03, 0x71, 0xB3, 0x55, 0x69, 0x49, 0xC8, 0x59, 0x54, 0x19, 0xE6, 0x21,
0x18, 0xA0, 0x3D, 0x30, 0x49, 0x71, 0x42, 0xD7, 0x36, 0x57, 0x0F, 0x7E, 0xCE, 0x03, 0x54, 0x41,
0x46, 0x17, 0xCD, 0xAC, 0x59, 0x54, 0x19, 0x46, 0xB3, 0x6A, 0x36, 0x0D, 0xAC, 0x28, 0xAD, 0x2A,
0x5B, 0x37, 0x5E, 0x7F, 0x77, 0x44, 0x12, 0x62, 0x53, 0x32, 0xD1, 0x51, 0x49, 0x51, 0xC4, 0x28,
0x06, 0xA6, 0x3D, 0xC8, 0x31, 0x35, 0x4C, 0x59, 0x76, 0x16, 0x36, 0x07, 0x7D, 0x27, 0x20, 0xC5,
0x5C, 0x42, 0x5E, 0xC3, 0x48, 0x08, 0xCD, 0x35, 0xC5, 0x2E, 0x3F, 0x59, 0x3C, 0x6D, 0x78, 0x4D,
0x00, 0x74, 0x46, 0x52, 0xD0, 0x43, 0x36, 0x4C, 0xD7, 0x45, 0x03, 0xC2, 0x32, 0xA5, 0x20, 0x54,
0x51, 0x31, 0x72, 0x72, 0x58, 0x65, 0x6F, 0x28, 0x29, 0xD7, 0x4A, 0x57, 0x3E, 0xC2, 0x5A, 0x77,
0xD0, 0x26, 0xA8, 0x2B, 0x5B, 0x56, 0x51, 0x7C, 0x19, 0x50, 0x68, 0x70, 0x22, 0x3C, 0xB2, 0x51,
0x39, 0x45, 0xC5, 0x53, 0x16, 0xA2, 0x33, 0xB7, 0x5F, 0x49, 0x42, 0x5C, 0x77, 0x16, 0x57, 0x08,
0x7E, 0x49, 0x34, 0xBF, 0x4E, 0x33, 0x50, 0xA0, 0x48, 0x78, 0xD9, 0x34, 0xBE, 0x3E, 0x3B, 0x57,
0x43, 0x03, 0x04, 0x43, 0x05, 0x75, 0x46, 0x33, 0xDF, 0x40, 0x58, 0x58, 0xAD, 0x57, 0x72, 0xCC,
0x51, 0xA5, 0x50, 0x40, 0x50, 0x4A, 0x62, 0x76, 0x56, 0x1A, 0x01, 0x54, 0x27, 0xD2, 0x4B, 0x57,
0x5F, 0xCD, 0x59, 0x19, 0xC4, 0x5C, 0xBA, 0x5A, 0x55, 0x35, 0x51, 0x0C, 0x0D, 0x51, 0x13, 0x60,
0x26, 0x32, 0xCD, 0x3F, 0x45, 0x4B, 0xC0, 0x52, 0x16, 0xC3, 0x3C, 0xB4, 0x31, 0x5D, 0x38, 0x4E,
0x06, 0x18, 0x34, 0x08, 0x0E, 0x5D, 0x35, 0xC4, 0x5E, 0x37, 0x5E, 0xDF, 0x26, 0x04, 0xD7, 0x31,
0xBF, 0x3E, 0x5A, 0x58, 0x40, 0x6D, 0x10, 0x39, 0x17, 0x04, 0x48, 0x50, 0xDF, 0x30, 0x4C, 0x59,
0xD6, 0x47, 0x0E, 0xDD, 0x63, 0x8C, 0x3A, 0xDB, 0x83, 0x4C, 0xB1, 0x49, 0x26, 0x86, 0x8B, 0xB7,
0x8B, 0x8E, 0xE2, 0x42, 0x36, 0x49, 0xF0, 0x68, 0x01, 0x9F, 0x41, 0xD0, 0xF3, 0x38, 0x46, 0xEA,
0xB8, 0x48, 0x33, 0x4F, 0x46, 0xBC, 0xE3, 0x16, 0x47, 0xDE, 0x9A, 0x55, 0x4D, 0x4A, 0x0E, 0xDF,
0xF7, 0x16, 0x87, 0xBD, 0xD3, 0x30, 0xDC, 0xE2, 0x32, 0xB3, 0x6A, 0x75, 0x64, 0x30, 0xBF, 0xB5,
0x2C, 0xEF, 0x4D, 0x79, 0x5D, 0xFB, 0x05, 0x85, 0xCD, 0xEE, 0x2A, 0x94, 0x00, 0xF3, 0xA5, 0x7F,
0xDC, 0x46, 0xB4, 0xDF, 0xA8, 0x30, 0x2A, 0xA8, 0x0C, 0x88, 0x7F, 0xA8, 0x18, 0x3A, 0xCF, 0x8F,
0x2A, 0xA7, 0xFA, 0xA0, 0xFC, 0x95, 0xF6, 0x78, 0xBC, 0x18, 0xB3, 0x3A, 0xAF, 0xAA, 0xBD, 0x18,
0xBE, 0x1E, 0x34, 0xCE, 0x0E, 0xBA, 0x8A, 0xE2, 0xDA, 0x96, 0x7B, 0x04, 0x71, 0x0D, 0x4D, 0xD3,
0x8D, 0xE4, 0x48, 0xC5, 0x25, 0x2B, 0x59, 0x36, 0xFC, 0xD0, 0x7C, 0x6B, 0x19, 0x22, 0x3D, 0xE6,
0x74, 0xB0, 0xAE, 0x2E, 0x5E, 0xED, 0xE1, 0x04, 0xF1, 0x83, 0x61, 0x33, 0x16, 0x3B, 0xDB, 0x81,
0xFA, 0x03, 0x05, 0x55, 0x73, 0x9A, 0x67, 0x76, 0x99, 0x11, 0x08, 0x55, 0xE6, 0x6A, 0x77, 0x0F,
0xF4, 0xF7, 0xDF, 0x50, 0x66, 0xC1, 0xFD, 0x56, 0xEB, 0xAA, 0x5E, 0xC9, 0x65, 0xD3, 0x22, 0x08,
0xD0, 0x45, 0xD0, 0x26, 0x87, 0x61, 0x3E, 0x18, 0x88, 0x68, 0xC4, 0x2D, 0x1E, 0x8F, 0x88, 0xA4,
0x3E, 0x3F, 0x28, 0x20, 0xEC, 0xFE, 0xB2, 0xE2, 0xBB, 0x7D, 0x66, 0xCC, 0x2D, 0x3C, 0xD5, 0xEB,
0xB2, 0xED, 0xD2, 0xC6, 0x01, 0xEB, 0x06, 0xE6, 0xD7, 0x7E, 0x92, 0x4E, 0x26, 0xAD, 0x8A, 0xAA,
0x98, 0x49, 0xEC, 0xAA, 0xA5, 0xC9, 0x6B, 0x10, 0x87, 0x34, 0x07, 0x4A, 0xA9, 0x1E, 0x3A, 0x12,
0x85, 0xEF, 0xD6, 0xC4, 0x21, 0xD8, 0x55, 0x96, 0x88, 0xC9, 0xDA, 0x2C, 0x66, 0xCC, 0x8D, 0xE5,
0xF7, 0x6A, 0x1B, 0x0B, 0x2C, 0x19, 0x7F, 0x16, 0xAA, 0x37, 0xCC, 0xD9, 0xF7, 0x1D, 0x13, 0x60,
0xC3, 0x3A, 0x5F, 0x60, 0x1F, 0xE8, 0x23, 0x77, 0x67, 0xB0, 0x9B, 0x86, 0x8C, 0xDC, 0x1E, 0x41,
0xB0, 0x06, 0x93, 0x4C, 0xA3, 0xB6, 0xBD, 0xF8, 0xB2, 0xBF, 0x3E, 0x8E, 0x19, 0x0C, 0x4A, 0x17,
0xEF, 0x10, 0x31, 0x43, 0x40, 0xFD, 0x6C, 0x62, 0xC2, 0x5A, 0x4E, 0x0F, 0x3D, 0x9F, 0x83, 0xEB,
0x8C, 0x2F, 0x71, 0xA8, 0x89, 0x84, 0xE4, 0x3E, 0xB7, 0x53, 0x97, 0x82, 0xD0, 0xE1, 0x3D, 0x4F,
0xAD, 0x1E, 0xD8, 0x7B, 0xB8, 0x71, 0xC2, 0xE3, 0x5B, 0xAA, 0x17, 0x59, 0xBC, 0x2A, 0x36, 0x30,
0x8B, 0xEC, 0xA3, 0x56, 0x47, 0x9B, 0x2A, 0x7A, 0x9D, 0x40, 0x24, 0xF4, 0x68, 0x27, 0xB8, 0x69,
0xBD, 0x75, 0x64, 0xD7, 0xBD, 0xD4, 0xF2, 0xBD, 0x31, 0xFC, 0x6C, 0xA0, 0xAE, 0x07, 0x0E, 0xF3,
0xC6, 0xE1, 0xFC, 0x4D, 0x1A, 0xF1, 0xCE, 0xF1, 0xFB, 0x65, 0xE9, 0x18, 0x97, 0x1B, 0xEF, 0x5A,
0x8D, 0xEC, 0x63, 0xA2, 0x58, 0x7C, 0xF2, 0x80, 0x50, 0xD3, 0x02, 0xEF, 0x58, 0xE9, 0x8B, 0x9B,
0x3C, 0xEF, 0x98, 0x9B, 0xE0, 0x32, 0x52, 0x2E, 0x92, 0x57, 0x07, 0xA6, 0xA8, 0x0A, 0x0F, 0xAC,
0xBD, 0xC7, 0x3B, 0xAD, 0xF8, 0x12, 0x39, 0x94, 0xF7, 0x38, 0x11, 0x7A, 0x22, 0xBB, 0x0C, 0xE9,
0x34, 0x77, 0x85, 0xF2, 0x7D, 0xA0, 0x58, 0xFE, 0x25, 0xB9, 0xF5, 0xCA, 0x04, 0x9D, 0x58, 0x4E,
0x47, 0xAE, 0x31, 0x12, 0x56, 0xB3, 0x2F, 0x98, 0x2D, 0x7C, 0x68, 0x6C, 0x90, 0xE9, 0x52, 0x65,
0xF2, 0x18, 0x8A, 0x9E, 0x60, 0x18, 0xD9, 0xFA, 0xC3, 0x25, 0x9A, 0xFA, 0x87, 0x32, 0x3C, 0x10,
0x27, 0x27, 0x40, 0xF6, 0xDF, 0xB1, 0x1B, 0x1D, 0xCD, 0xC3, 0xC8, 0x93, 0x34, 0x26, 0xF1, 0x08,
0x4C, 0xAF, 0x58, 0x77, 0x09, 0x60, 0xF7, 0x62, 0xCE, 0x52, 0x9F, 0x2E, 0x52, 0xDF, 0x99, 0x28,
0x88, 0x1F, 0xE1, 0x98, 0x65, 0xD4, 0xE7, 0xF9, 0x82, 0xB9, 0x72, 0xFD, 0x14, 0x1D, 0x66, 0x34,
0xAB, 0xC1, 0xE1, 0x2F, 0x46, 0x27, 0xA7, 0x08, 0x9B, 0xD1, 0xA0, 0x6B, 0xA5, 0x1E, 0x77, 0xAC,
0x2E, 0x54, 0xFD, 0x55, 0xA3, 0x89, 0xAC, 0x5A, 0xAC, 0x23, 0x7B, 0xB9, 0x15, 0x77, 0x9A, 0x58,
0x18, 0x97, 0xF4, 0x10, 0xFC, 0x01, 0x1C, 0x05, 0x13, 0xDC, 0x25, 0x9B, 0x78, 0xD6, 0x39, 0x35,
0x83, 0x4C, 0x2E, 0x09, 0x0E, 0xDF, 0x5F, 0xE9, 0x56, 0x64, 0xDB, 0xAF, 0xE2, 0x1C, 0x11, 0x02,
0x2B, 0x0B, 0x76, 0x97, 0xB1, 0x87, 0x55, 0x4B, 0xCC, 0x9A, 0x68, 0x1C, 0x2F, 0x46, 0x63, 0x93,
0x26, 0x41, 0x09, 0x1D, 0xF4, 0xB0, 0x52, 0x35, 0xE0, 0x21, 0x7A, 0x00, 0xA2, 0xFD, 0x41, 0x74,
0x1E, 0x19, 0x9B, 0xE8, 0xEA, 0xEA, 0x1C, 0xA1, 0xDA, 0x63, 0x86, 0x39, 0xC0, 0x39, 0xBA, 0xAB,
0xBE, 0xC0, 0x75, 0xF0, 0xC6, 0x1E, 0x15, 0xD4, 0x38, 0x27, 0x7B, 0xD7, 0x6B, 0xB7, 0x4A, 0x0E,
0x8F, 0x8E, 0x7A, 0x3D, 0x1C, 0xD5, 0x65, 0x59, 0x32, 0x85, 0x1C, 0xC5, 0xE3, 0xC4, 0x40, 0xAB,
0x71, 0xA6, 0xDA, 0x61, 0x8A, 0x09, 0x1A, 0x0B, 0x2B, 0xEE, 0x7D, 0x02, 0xFF, 0xD8, 0xAB, 0x8B,
0x7A, 0x4A, 0x4B, 0x66, 0x9B, 0x14, 0x12, 0x3F, 0xB9, 0x73, 0x2E, 0x2E, 0x9C, 0x76, 0xFC, 0x9D,
0xC0, 0x87, 0x92, 0x4F, 0x00, 0x53, 0xC2, 0xB8, 0x72, 0xFE, 0xE4, 0x7D, 0xE4, 0x6C, 0x9A, 0xC8,
0xA4, 0x1E, 0xF2, 0x4C, 0x51, 0x11, 0xEF, 0x21, 0x07, 0xF9, 0x73, 0xA3, 0x09, 0x95, 0x21, 0xBC,
0xEE, 0x02, 0x71, 0x50, 0xD7, 0x99, 0x38, 0xFA, 0xAB, 0x08, 0xAF, 0x16, 0x19, 0x0E, 0xA6, 0x08,
0x67, 0x6F, 0x17, 0xE2, 0xC2, 0x2B, 0xB8, 0xB4, 0xF2, 0xF6, 0x56, 0x39, 0xFD, 0xFE, 0x4E, 0xB6,
0xFB, 0x99, 0xAF, 0xA3, 0xB0, 0x94, 0x9B, 0xEC, 0x19, 0xEE, 0xA9, 0x16, 0x91, 0x5D, 0x3C, 0xBE,
0x27, 0xA3, 0xAB, 0x1C, 0x3D, 0xB6, 0xDC, 0x74, 0xB9, 0x2F, 0x46, 0x1D, 0x1C, 0x33, 0xFC, 0xF8,
0x0C, 0x23, 0xA9, 0x7B, 0xEA, 0xFF, 0x50, 0x43, 0x18, 0x34, 0x17, 0x3C, 0xF7, 0xAF, 0x9C, 0xA4,
0xC3, 0x2A, 0xD2, 0x2D, 0xA1, 0xA8, 0x8A, 0x64, 0x2B, 0xB6, 0x49, 0xB2, 0xBB, 0x56, 0x0C, 0x00,
0xDD, 0xF1, 0xF6, 0xCB, 0x67, 0xCC, 0x6D, 0x36, 0xB2, 0x31, 0xDE, 0x43, 0x88, 0xE9, 0x76, 0x29,
0x72, 0x0D, 0x3D, 0xAB, 0x04, 0xF4, 0x9B, 0x20, 0xCE, 0xAB, 0x69, 0xC5, 0x54, 0x63, 0x76, 0x2A,
0xA2, 0x29, 0x32, 0x2C, 0x0A, 0x29, 0xF1, 0xEA, 0x44, 0xB6, 0x03, 0x39, 0x15, 0x12, 0x68, 0x8C,
0xF4, 0xA6, 0xF0, 0x6D, 0x3B, 0x52, 0x20, 0x39, 0xDC, 0x2A, 0x33, 0xEF, 0xD5, 0xB5, 0xE7, 0x99,
0x66, 0x89, 0x0C, 0xCE, 0xB4, 0x2D, 0x9D, 0x9A, 0xCE, 0xCF, 0xF8, 0xA7, 0x37, 0x11, 0xF3, 0x6D,
0xAF, 0xBC, 0x48, 0x5D, 0x3D, 0xF0, 0x61, 0x02, 0x41, 0x07, 0x4C, 0x7A, 0x86, 0x30, 0xD9, 0xE2,
0xF3, 0xA0, 0xAC, 0xA2, 0x85, 0xB3, 0x08, 0xBB, 0x14, 0x86, 0xE0, 0x1E, 0xDD, 0xAA, 0xB6, 0xD6,
0x85, 0x44, 0x1F, 0xDF, 0x66, 0x27, 0x13, 0x4A, 0xF2, 0x5C, 0xE5, 0xC2, 0x35, 0xF8, 0xA4, 0xEE,
0x2A, 0x90, 0xA2, 0x3E, 0xB6, 0xA9, 0x75, 0xED, 0xE5, 0x14, 0x1F, 0xC2, 0xEC, 0xFD, 0x1D, 0x8A,
0x5D, 0x06, 0xCF, 0xA7, 0x47, 0xBF, 0xE3, 0x12, 0xCB, 0x6B, 0xA9, 0x1B, 0xBD, 0x4D, 0x83, 0x99,
0x0F, 0xFC, 0x43, 0x05, 0x8A, 0xF2, 0xD3, 0x45, 0xAB, 0x11, 0x98, 0x8F, 0x3C, 0xD5, 0xBA, 0xBA,
0x59, 0x98, 0xCC, 0xC3, 0x54, 0x96, 0xDD, 0xCF, 0x79, 0xCC, 0x01, 0xD1, 0xAA, 0xF7, 0xC2, 0xC8,
0xB8, 0xDF, 0xA8, 0xED, 0x72, 0x9D, 0xD1, 0x7F, 0x83, 0x32, 0xDB, 0xD7, 0x47, 0xC0, 0x27, 0x2A,
0xD9, 0x57, 0x8E, 0x93, 0x7C, 0xFC, 0x4C, 0x9C, 0x98, 0x39, 0xCE, 0xC4, 0xB3, 0x3C, 0x88, 0xF6,
0xBD, 0xB2, 0x91, 0xC2, 0x9E, 0x3E, 0x60, 0x15, 0xB6, 0xCF, 0xB3, 0x9D, 0x98, 0xE7, 0xD7, 0x27,
0x9E, 0xFD, 0xA3, 0xFE, 0xAF, 0x3E, 0x94, 0x13, 0x83, 0x53, 0x90, 0xFE, 0xEE, 0xC1, 0xC5, 0xF6,
0x4C, 0x6E, 0x2F, 0x72, 0x42, 0xAD, 0x27, 0x9D, 0xF1, 0xCE, 0xBD, 0xF6, 0x7C, 0x47, 0x72, 0xAE,
0x28, 0xBF, 0x00, 0xB0, 0x29, 0x9F, 0x02, 0x08, 0x2E, 0xBE, 0xB4, 0x4B, 0x7A, 0x29, 0xAD, 0x95,
0xC3, 0x69, 0x83, 0xD8, 0x35, 0x88, 0xFF, 0x85, 0x60, 0x9F, 0xCA, 0xCF, 0xB0, 0xF5, 0xCE, 0x6A,
0x52, 0x8D, 0xCB, 0x0E, 0x8D, 0x70, 0x03, 0x8E, 0xAC, 0xF2, 0xA3, 0xA4, 0xF0, 0xAE, 0x67, 0x36,
0xB4, 0x48, 0xA0, 0xB9, 0x51, 0xE3, 0x76, 0x85, 0x05, 0xB6, 0xB2, 0x4A, 0x37, 0xA5, 0xBA, 0xCF,
0xFC, 0x6E, 0xBD, 0x7E, 0xA0, 0x71, 0x38, 0xE4, 0xFF, 0x1A, 0x19, 0xF3, 0x1C, 0x3D, 0x47, 0x99,
0x39, 0x17, 0x74, 0xDA, 0xC6, 0x25, 0x35, 0x93, 0xA8, 0xAE, 0xFA, 0x83, 0x12, 0xDF, 0xE1, 0x66,
0x01, 0x2B, 0x63, 0x56, 0x56, 0x2A, 0x4C, 0x49, 0xF5, 0x80, 0xD6, 0xE2, 0x79, 0x3C, 0x19, 0xF8,
0x57, 0x50, 0x06, 0x3F, 0x1B, 0x74, 0xBF, 0x30, 0x46, 0x53, 0x64, 0x04, 0x56, 0x06, 0xC3, 0x43,
0x50, 0x4D, 0xBB, 0x46, 0x36, 0xF4, 0x25, 0x19, 0xAC, 0x9B, 0x73, 0x00, 0x29, 0x16, 0x56, 0x4A,
0x44, 0x40, 0x53, 0xF1, 0xFA, 0xC6, 0x87, 0x78, 0x40, 0x19, 0x90, 0x23, 0x47, 0x76, 0x31, 0x19,
0x7B, 0xCC, 0x4A, 0x53, 0x52, 0x66, 0x71, 0x56, 0x1A, 0xAD, 0x4F, 0x4A, 0x49, 0xC1, 0x56, 0x53,
0xF5, 0x59, 0x19, 0xC4, 0xEF, 0x64, 0x70, 0x27, 0x14, 0x59, 0x39, 0x3E, 0x55, 0x52, 0xF3, 0x8F,
0xC6, 0x9B, 0x16, 0x4C, 0x03, 0x94, 0x59, 0x57, 0x13, 0x30, 0x65, 0x7B, 0xA4, 0x3E, 0x44, 0x22,
0x68, 0x73, 0x59, 0x69, 0xD7, 0x5A, 0x4B, 0x4B, 0xB4, 0x56, 0x4F, 0x9B, 0x55, 0x03, 0xC0, 0x95,
0x74, 0x15, 0x26, 0x68, 0x59, 0x51, 0x4A, 0x42, 0x22, 0xFD, 0x8D, 0xC9, 0xE8, 0x6C, 0x59, 0x02,
0x96, 0x2C, 0x57, 0x0F, 0x5E, 0x69, 0x61, 0xA0, 0x44, 0x54, 0x47, 0x69, 0x0F, 0x59, 0x01, 0xA3,
0x4D, 0x3B, 0x45, 0xB6, 0x59, 0x3C, 0xE1, 0x40, 0x02, 0xC2, 0xE0, 0x74, 0x09, 0x48, 0x64, 0x43,
0x55, 0x30, 0x52, 0x47, 0xFC, 0xF1, 0xC9, 0x80, 0x18, 0x4E, 0x72, 0x98, 0x2E, 0x58, 0x7C, 0x24,
0x7C, 0x60, 0xA2, 0x31, 0x54, 0x5B, 0x07, 0x03, 0x43, 0x05, 0xD9, 0x5D, 0x5E, 0x44, 0xCA, 0x59,
0x54, 0x95, 0x57, 0xCA, 0x5F, 0xF8, 0xC0, 0x2E, 0x82, 0x9F, 0x91, 0xF8, 0xEE, 0x56, 0x4B, 0x37,
0x44, 0x0A, 0x11, 0x0D, 0x12, 0xF9, 0x1B, 0x28, 0xDB]

# expected first 16 bits
ex = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52]
expected = ""
for i in ex:
	expected = expected + chr(i)

flag = ""

possibilities = []
f = 1

# expected input characters
compatiblestring = string.ascii_uppercase + string.digits

# bruteforcing rest 9 characters of the input and checking if all of them are printable
for i in range(500):
	for j in range(500):
		tempexpected = ""
		tempexpected = expected + chr(0x00) + chr(0x00 )+ chr(i >> 8) + chr(i % 256) + chr(0x00) + chr(0x00) + chr(j>>8) + chr(j % 256) + chr(0x8)
		f = 1
		tempkey = ""
		for k in range(len(tempexpected)):
			temp = chr(ord(tempexpected[k]) ^ encrypted[k])
			if temp not in compatiblestring:
				f = 0
				break
			else:
				tempkey = tempkey + temp
		if f == 1:
			possibilities.append(tempkey)

# all the input possibilities that have PNG signature
print len(possibilities)

counter = 0

# Writing PNG files after decrypting with the possible keys

for key in possibilities:
	decoded = ""
	for i in range(len(encrypted)):
		decoded = decoded + chr(encrypted[i] ^ ord(key[i % len(key)]))
	name = 'decoded_%d' %counter
	name = name + '.png'
	fileo = open(name, 'wb')
	fileo.write(decoded)
	fileo.close()
	counter = counter + 1

# Finding out valid PNG images among created images.
count = 0
for i in range(len(possibilities)):
	try:
		name = 'decoded_%d.png' %i
		im = Image.open(name)
		print("check: " + name)
		break
	except IOError:
		count = count + 1
