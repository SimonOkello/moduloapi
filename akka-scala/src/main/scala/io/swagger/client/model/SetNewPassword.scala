/**
 * Modulo API
 * Test description
 *
 * OpenAPI spec version: v1
 * Contact: simonokello93@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.model

import io.swagger.client.core.ApiModel
import org.joda.time.DateTime
import java.util.UUID

case class SetNewPassword (
  password: String,
  uidb64: String,
  token: String
) extends ApiModel


