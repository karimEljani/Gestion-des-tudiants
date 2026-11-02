using MesClasses;
using Microsoft.EntityFrameworkCore;

namespace EmployeeWebAPI.Models
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<Employee> Employees { get; set; }
        public DbSet<Department> Departments { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Données initiales : départements
            modelBuilder.Entity<Department>().HasData(
                new Department { DepartmentId = 1, DepartmentName = "IT" },
                new Department { DepartmentId = 2, DepartmentName = "HR" },
                new Department { DepartmentId = 3, DepartmentName = "Payroll" },
                new Department { DepartmentId = 4, DepartmentName = "Admin" });

            // Données initiales : employés
            modelBuilder.Entity<Employee>().HasData(
                new Employee
                {
                    EmployeeId = 1,
                    FirstName = "ZRIBI",
                    LastName = "MALEK",
                    Email = "malek_zribi@yahoo.fr",
                    DateOfBrith = new DateTime(1976, 5, 10),
                    Gender = Gender.Female,
                    DepartmentId = 1,
                    PhotoPath = null
                },
                new Employee
                {
                    EmployeeId = 2,
                    FirstName = "TRIKI",
                    LastName = "MOHAMED ALI",
                    Email = "triki_ali@gmail.com",
                    DateOfBrith = new DateTime(1988, 5, 22),
                    Gender = Gender.Male,
                    DepartmentId = 2,
                    PhotoPath = null
                });
        }
    }
}
