/*
 * Swagger Petstore
 *
 * A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification
 *
 * API version: 1.0.0
 * Contact: apiteam@swagger.io
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

type PetAllOf struct {

	Id int64 `json:"id"`
}

// AssertPetAllOfRequired checks if the required fields are not zero-ed
func AssertPetAllOfRequired(obj PetAllOf) error {
	elements := map[string]interface{}{
		"id": obj.Id,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertRecursePetAllOfRequired recursively checks if required fields are not zero-ed in a nested slice.
// Accepts only nested slice of PetAllOf (e.g. [][]PetAllOf), otherwise ErrTypeAssertionError is thrown.
func AssertRecursePetAllOfRequired(objSlice interface{}) error {
	return AssertRecurseInterfaceRequired(objSlice, func(obj interface{}) error {
		aPetAllOf, ok := obj.(PetAllOf)
		if !ok {
			return ErrTypeAssertionError
		}
		return AssertPetAllOfRequired(aPetAllOf)
	})
}
