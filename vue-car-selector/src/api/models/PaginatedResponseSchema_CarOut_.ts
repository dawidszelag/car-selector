/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { CarOut } from './CarOut';

/**
 * Abstract base class for generic types.
 *
 * A generic type is typically declared by inheriting from
 * this class parameterized with one or more type variables.
 * For example, a generic mapping type might be defined as::
 *
 * class Mapping(Generic[KT, VT]):
 * def __getitem__(self, key: KT) -> VT:
 * ...
 * # Etc.
 *
 * This class can then be used as follows::
 *
 * def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
 * try:
 * return mapping[key]
 * except KeyError:
 * return default
 */
export type PaginatedResponseSchema_CarOut_ = {
    count: number;
    next?: string;
    previous?: string;
    results: Array<CarOut>;
};

