using System.ComponentModel.DataAnnotations;

namespace MesClasses
{
    public class Employee
    {
        public int EmployeeId { get; set; }

        [Required]
        [StringLength(100, MinimumLength = 2)]
        public string FirstName { get; set; } = string.Empty;

        [Required]
        public string LastName { get; set; } = string.Empty;

        [Required]
        [EmailAddress]
        public string Email { get; set; } = string.Empty;

        public DateTime DateOfBrith { get; set; }
        public Gender Gender { get; set; }
        public int DepartmentId { get; set; }
        public string? PhotoPath { get; set; }
        public Department? Department { get; set; }
    }
}
