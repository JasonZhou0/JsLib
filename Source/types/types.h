/*!
* \addtogroup MCU_COMMON
* \{
*
* \file     types.h
*
* \brief    types internal interface.
*
* Copyright (c) 2015 Autoliv Electronics AB
*
* All rights reserved. Property of Autoliv Electronics AB.
* Restricted rights to use, duplicate or disclose this code
* are granted through contract.
*/

#ifndef TYPES_H
#define TYPES_H

/* **** Includes **** */

/* **** Defines **** */

#ifndef AlvTrue
#ifdef QAC
#pragma PRQA_MACRO_MESSAGES_OFF "AlvTrue" 4330, 1056
#define AlvTrue (_Bool)1 /* ALV S MACRO_NAME */
#else
#define AlvTrue 1 /* ALV S MACRO_NAME */
#endif
#endif

#ifndef AlvFalse
#ifdef QAC
#pragma PRQA_MACRO_MESSAGES_OFF "AlvFalse" 4330, 1056
#define AlvFalse (_Bool)0 /* ALV S MACRO_NAME */
#else
#define AlvFalse 0 /* ALV S MACRO_NAME */
#endif
#endif

#define AlvNull  ((void*)0) /* ALV S MACRO_NAME */

#define TRUE   1
#define FALSE  0
#define NULL   ((void*)0)

/* Floating point value constants */
#define F32_ZERO (0.0f)
#define F32_HALF (0.5f)
#define F32_ONE  (1.0f)

/* Integer limit constants */
#define S8_MIN  (-128)
#define S8_MAX  (127)
#define U8_MIN  (U8)(0x00u)
#define U8_MAX  (U8)(0xFFu)
#define S16_MIN (-32768)
#define S16_MAX (32767)
#define U16_MIN (U16)(0x0000u)
#define U16_MAX (U16)(0xFFFFu)
#define S32_MIN (-2147483647 - 1)
#define S32_MAX (2147483647)
#define U32_MIN (0x00000000u)
#define U32_MAX (0xFFFFFFFFu)
#define U64_MIN (0x0000000000000000uLL)
#define U64_MAX (0xFFFFFFFFFFFFFFFFuLL)
#define S64_MIN (-9223372036854775807LL - 1LL)
#define S64_MAX (9223372036854775807LL)

/* AlvChar size constants */
#define ALVCHAR_NO_BITS  (8u)
#define ALVCHAR_NO_BYTES (1u)

/* Integer size constants */
#define U8_NO_BITS       (8u)
#define U8_NO_BYTES      (1u)
#define S8_NO_BITS       (U8_NO_BITS)
#define S8_NO_BYTES      (U8_NO_BYTES)
#define U16_NO_BITS      (16u)
#define U16_NO_BYTES     (2u)
#define S16_NO_BITS      (U16_NO_BITS)
#define S16_NO_BYTES     (U16_NO_BYTES)
#define U32_NO_BITS      (32u)
#define U32_NO_BYTES     (4u)
#define S32_NO_BITS      (U32_NO_BITS)
#define S32_NO_BYTES     (U32_NO_BYTES)
#define U64_NO_BITS      (64u)
#define U64_NO_BYTES     (8u)
#define S64_NO_BITS      (U64_NO_BITS)
#define S64_NO_BYTES     (U64_NO_BYTES)
#define F32_NO_BITS      (32u)
#define F32_NO_BYTES     (4u)

/* ASCII element constants */
#define CHAR_NUL              '\0'
#define CHAR_BACKSPACE        '\b'
#define CHAR_CARRIAGE_RETURN  '\r'
#define CHAR_TAB              '\t'
#define CHAR_SPACE            ' '
#define CHAR_PLUS             '+'
#define CHAR_MINUS            '-'
#define CHAR_DOT              '.'
#define CHAR_PERCENT          '%'
#define CHAR_OC_BRACKET       '{'
#define CHAR_CC_BRACKET       '}'
#define CHAR_ZERO             '0'
#define CHAR_NINE             '9'
#define CHAR_UPPER_A          'A'
#define CHAR_UPPER_F          'F'
#define CHAR_UPPER_Z          'Z'
#define CHAR_LOWER_A          'a'
#define CHAR_LOWER_B          'b'
#define CHAR_LOWER_C          'c'
#define CHAR_LOWER_D          'd'
#define CHAR_LOWER_F          'f'
#define CHAR_LOWER_I          'i'
#define CHAR_LOWER_S          's'
#define CHAR_LOWER_U          'u'
#define CHAR_LOWER_X          'x'
#define CHAR_LOWER_Z          'z'

/* String constants */
#define NEWLINE               "\r\n"
#define EMPTY_STRING          ""

/* Math constants */
#define MATH_PI               (3.1415927f)

/* Time conversion constants */
#define HOURS_PER_DAY         (24u)
#define MINUTES_PER_HOUR      (60u)
#define SECONDS_PER_HOUR      ((SECONDS_PER_MINUTE) * (MINUTES_PER_HOUR))
#define SECONDS_PER_MINUTE    (60u)
#define MS_PER_S              (1000u)
#define US_PER_S              ((US_PER_MS) * (MS_PER_S))
#define US_PER_MS             (1000u)
#define NS_PER_S              ((NS_PER_MS) * (MS_PER_S))
#define NS_PER_MS             ((NS_PER_US) * (US_PER_MS))
#define NS_PER_US             (1000u)

/* Length conversion constants */
#define MM_PER_M              (1000u)
#define M_PER_KM              (1000u)

/* Speed conversion constants */
#define MPS_PER_KMPH          (3.6f)
#define MPH_PER_MPS           (0.44704f)
#define MPH_PER_KMPH          (1.609344f)

/* Angle conversion constants */
#define DEGREES_PER_RADIAN_F32  (180.0f / MATH_PI)

/* General unit conversion constants */
#define UNITS_PER_GIGA_UNIT   (1000000000u)
#define UNITS_PER_MEGA_UNIT   (1000000u)
#define UNITS_PER_KILO_UNIT   (1000u)
#define DECI_UNITS_PER_UNIT   (10u)
#define CENTI_UNITS_PER_UNIT  (100u)
#define MILLI_UNITS_PER_UNIT  (1000u)
#define MICRO_UNITS_PER_UNIT  (1000000u)
#define NANO_UNITS_PER_UNIT   (1000000000u)

/* Casting constants */
#pragma PRQA_MACRO_MESSAGES_OFF "P_CHAR", 310, 311
#define P_CHAR             (AlvChar*)
#pragma PRQA_MACRO_MESSAGES_OFF "CONST_P_CHAR", 310, 3631
#define CONST_P_CHAR       (const AlvChar*)
#pragma PRQA_MACRO_MESSAGES_OFF "P_U8", 310, 311
#define P_U8               (U8*)
#pragma PRQA_MACRO_MESSAGES_OFF "CONST_P_U8", 310, 311
#define CONST_P_U8         (const U8*)
#pragma PRQA_MACRO_MESSAGES_OFF "CONST_P_U8_CONST", 310, 311
#define CONST_P_U8_CONST   (const U8* const)

#if defined(__TASKING__) || defined(__GNUC__) || defined(_MSC_VER)
/*! \qacexception 1055: The keyword 'inline' has been used. REFERENCE - ISO:C99-6.7.4 Function specifiers
 *                      This is used for optimizations.
 */
#pragma PRQA_MACRO_MESSAGES_OFF "ALV_INLINE" 1055
#define ALV_INLINE   static inline
#define ALV_RESTRICT restrict
#else
#error "Unsupported compiler"
#endif

/* **** Typedefs **** */

#if defined(__TASKING__) || defined(__GNUC__) || defined(_MSC_VER)
/*! \qacexception 3632: Type 'char' has been used in the declaration of a typedef. REFERENCE - ISO:C90-6.1.2.5 Types
 *                      This is our definition of our own type of a character type that is used for text strings.
 *                      AlvChar is only used for text strings and not to store any values and it is therefore no risk of
 *                      confusion about the sign of the AlvChar type.
 */
typedef char               AlvChar; /* PRQA S 3632 */
typedef unsigned char      AlvBool; /*    AlvFalse .. AlvTrue         */
typedef signed char        S8;      /*        -128 .. +127            */
typedef unsigned char      U8;      /*           0 .. 255             */
typedef signed short       S16;     /*      -32768 .. +32767          */
typedef unsigned short     U16;     /*           0 .. 65535           */
typedef signed long        S32;     /* -2147483648 .. +2147483647     */
typedef unsigned long      U32;     /*           0 .. 4294967295      */
typedef signed long long   S64;     /* -9223372036854775807 .. +9223372036854775807     */
typedef unsigned long long U64;     /*                    0 .. 18446744073709551615     */
typedef float              F32;     /*        -3.402823e+38 .. +3.402823e+38            */
typedef double             F64;     /*        -3.402823e+38 .. +3.402823e+38            */


typedef signed char        bool;    /*        -128 .. +127            */
typedef signed char        s8;      /*        -128 .. +127            */
typedef unsigned char      u8;      /*           0 .. 255             */
typedef signed short       s16;     /*      -32768 .. +32767          */
typedef unsigned short     u16;     /*           0 .. 65535           */
typedef signed long        s32;     /* -2147483648 .. +2147483647     */
typedef unsigned long      u32;     /*           0 .. 4294967295      */
typedef signed long long   s64;     /* -9223372036854775807 .. +9223372036854775807     */
typedef unsigned long long u64;     /*                    0 .. 18446744073709551615     */
typedef float              f32;     /*        -3.402823e+38 .. +3.402823e+38            */
typedef double             f64;     /*        -3.402823e+38 .. +3.402823e+38            */
#else
#error "Unsupported compiler"
#endif

/* **** Extern Variables **** */

/* **** Function Declarations **** */

#endif /* TYPES_H */
/*! \} */
