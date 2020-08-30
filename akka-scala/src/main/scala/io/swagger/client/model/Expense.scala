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

case class Expense (
  id: Option[Int] = None,
  category: ExpenseEnums.Category,
  description: String,
  amount: String,
  date: Date
) extends ApiModel

object ExpenseEnums {

  type Category = Category.Value
  object Category extends Enumeration {
    val Travel = Value("Travel")
    val Rent = Value("Rent")
    val Food = Value("Food")
    val Internet = Value("Internet")
    val Electricity = Value("Electricity")
    val Vacation = Value("Vacation")
    val Netflix = Value("Netflix")
    val Other = Value("Other")
  }

}

